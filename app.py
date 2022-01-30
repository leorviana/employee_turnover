import numpy as np
import pandas as pd
import pickle
import streamlit as st
from scalers.data_prep import preprocessing


#Loading scaler
scaler = preprocessing()

#Loading model
model = pickle.load(open("model/employee_model.pkl", "rb"))

def main():
    st.title("Employee Turnover Probability")
    c = st.container()
    education_level = c.select_slider("Education Level", ["Bachelors", "Masters", "PHD"])
    payment_level = c.slider("Payment Tier", 1, 3)
    time_employed = c.slider("Years employed", 0, 10)
    
    gender = c.selectbox("Gender", ["Male", "Female"])
    if gender == "Female":
        gender = 1
    else:
        gender = 0
    
    ever_benched = c.selectbox("Did the employee ever benched?", ["No", "Yes"])
    if ever_benched == "Yes":
        ever_benched = 1
    else:
        ever_benched = 0
        
    city = c.selectbox("City", ["Bangalore", "Pune", "New Delhi"])
    
    age = c.number_input("Age", 18, 60)

    
    entrada = np.array([education_level, payment_level, age, gender, ever_benched, time_employed, city])
    entrada = entrada.reshape(1, -1)
    
    df_init = pd.DataFrame(entrada, columns=["education", "payment_tier", "age", "gender", "ever_benched", "time_employed", "city"])
    
    c2 = st.container()
    if c2.button("Turnover Probability"):
        
        entrada = (scaler.scaling(df_init)).values.reshape(1, -1)
        predicao = model.predict_proba(entrada)[:, 1]
        predicao = predicao.round(2)
        c2.success("{} %".format(predicao * 100))
    
    
if __name__ == "__main__":
    main()