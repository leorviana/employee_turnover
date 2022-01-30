import pickle
import pandas as pd

class preprocessing(object):
    def __init__(self):
        self.education_label = pickle.load(open("scalers/label_encoder_education.pkl", "rb"))
        self.age_minmax = pickle.load(open("scalers/age_encoder.pkl", "rb"))
        self.payment_minmax = pickle.load(open("scalers/payment_tier_encoder.pkl", "rb"))
        self.employed_minmax = pickle.load(open("scalers/time_employed_encoder.pkl", "rb"))
        self.education_minmax = pickle.load(open("scalers/education_encoder.pkl", "rb"))
        self.city_ohe = pickle.load(open("scalers/ohe_city.pkl", "rb"))
        
        
    def scaling(self, df):
        df["education"] = self.education_label.transform(df["education"].values.reshape(-1, 1))
        df["age"] = self.age_minmax.transform(df["age"].values.reshape(-1, 1))
        df["payment_tier"] = self.payment_minmax.transform(df["payment_tier"].values.reshape(-1, 1))
        df["time_employed"] = self.employed_minmax.transform(df["time_employed"].values.reshape(-1, 1))
        df["education"] = self.education_minmax.transform(df["education"].values.reshape(-1, 1))
        df_temp = pd.DataFrame(self.city_ohe.transform(df["city"].values.reshape(-1,1)).toarray(), columns = ["city_" + str(x) for x in self.city_ohe.categories_[0]])
        df = pd.concat([df, df_temp], axis = 1)
        df = df.drop("city", axis = 1)
        
        return df