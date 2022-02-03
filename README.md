# Employee Turnover

![alt text](https://static.6minutos.uol.com.br/2020/07/shutterstock_1358694809-768x506.jpg)

# Business Question
<b>The data below, as well as its context, is completely fictitious.</b>

In a meeting with the human resources team of the company we work for, we were informed that many employees leave the company after two years. 

It was reported that the cost of leaving one employee and hiring another is approximately $15000.00. In addition, we lose productivity in the periods between the departure of an employee and the entry of another

Our goal is then to help identify employees who are most likely to leave the company. The thought solution was to develop a probability estimation model.

# Project

## Project planning

### Problematic
Many employees leave the company after two years. 

It was reported that the cost of leaving one employee and hiring another is approximately $15000.00. In addition, we lose productivity in the periods between the departure of an employee and the entry of another.

### Solution
Our goal is to provide a model in production for the human resources team, in addition it would be interesting if we wrote a report with some insights into the phenomena that may be influencing the dismissal of these employees.

Based on information about the employee, the model should return an estimate of the probability of that employee leaving the company in the next two years.

### Sucess Criteria
The model must be better than we decide by luck who will leave the company, that is, the model must have more than 50% of accuracy.

### Useful Data
We were given a csv file with 4653 records about different employees who are in the company and who have also left. The data contains information about the employee's contract as well as geographic and personal information.

### Users
The human resources team.

### Use
With the identification of employees who are likely to leave the company, the human resources team can carry out some treatment with those employees who present a high possibility of leaving the company, in addition we can choose which employees to hire in order to avoid future turnovers.

### Integration
They will be able to access the model and its predictions online in a web app developed with streamlit and python.
After providing the information about the employee, the model returns the 2-year turnover probability.

### Key Actors
- Human Resources Team
- CEO
- Data Science Team

### Constraints
The amount of data about the event is relatively small and it is impossible to collect more. 

### Business Advantages
The human resources team will use the predictions given by the model and take care of employees who have a high probability of leaving the company, perhaps offering bonuses, a better career plan, among other things. Each employee who avoids leaving is saved an average of $15,000.00 with the process of leaving and hiring a new person.

### Cost Structure
Data Scientist salary.

## Procedure
 
### What are the characteristics of the employees who leave the company?
 
 To answer this question the following steps will be followed:

- Collect data in Kaggle;
- Clean the data;
- Feature engineering;
- Performing an exploratory analysis we will look for the best features that describe a turnover employee.
- Return this in a report.

### Once the best features have been identified, how do we construct the model?
 
 To construct the model, the following steps will be followed:

- Data preprocessing(OneHotEncoding, normalization, imbalanced data);
- Feature selection;
- Modeling and choosing the best estimator;
- Hiperparameter tuning;
- Evaluating final model on test data;
- Deploy the model to consumption;

## Tools 
 <p>
  <ul>
    <li><a href="https://www.python.org/">Python 3.9</a></li>
    <li><a href="https://jupyter.org/">Jupyter Notebook</a></li>
  </ul>
 </p>
 
 
# Results

## Insights Report
### 1. Employees with less time into the company
Employees who left the company have an average of years in the company of 2.46 years while who doesn't left have an average of years of 3.18.
<p align="left">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/time_employed.png">
</p>

### 2. Employees with Master degree
48,8% of the employees with Master Degree left the company.
<p align="left">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/education.png">
</p>

### 3. Employees from Pune
50,4% of the employees from Pune left the company.
<p align="left">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/pune.png">
</p>

### 4. Employees with median level payment
59,9% of the employees with median level payment left the company.
<p align="left">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/payment_tier.png">
</p>

### 5. Female employees
47% of the female employees left the company.
<p align="left">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/female.png">
</p>

### 6. Employees who benched
45,4% of the employees who ever benched left the company.
<p align="left">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/ever_benched.png">
</p>

# Model

### Model Type
Random Forest Regressor in production that gives de probability of a turnover.

### Integration
Streamlit Web App

### Used Features
- education	-
- payment_tier 
- age
- gender
- ever_benched
- time_employed
- city

### Maintenance
The model must be retrained with new data every 6 months or a year, depending on how many employees left the company in this period.

### Final Model Performance
- balanced_accuracy_score: 0.83
- f1_score: 0.77
- recall_score: 0.75
- precision_score: 0.80

## Model Deploy
You can access the web app developed to provide the model and use it through the link: 
<https://share.streamlit.io/leorviana/employee_turnover/main/app.py>.

# Business Evaluation

The average cost of terminating and hiring a new employee to replace is $15000.00
With this model we were able to identify employees who are about to leave and try to recover them before then.

As we can see, our model can identify correctly 75% of the employees that will turnover in the future. If we consider that we can retain only 50% of the employees that our model identify, our model can reduce the expected loss of employee from $15000 to 9475.00, a reduce of 36%.

# Conclusion

At the end of this project it was possible to reach a very good number for reducing the spending of human resources company sector, the human resources manager now has in hand which characteristics a employee that will left the company has and a model that predict if a specific employee will turnover, being thus it is correct to say that the main objective of this project was successfully achieved.

# Next steps

To further improve the model and generate more accurate predictions, we may collect more data and seek to identify other employee characteristics.

# References

Employee Future Prediction. Kaggle. Available on: <https://www.kaggle.com/tejashvi14/employee-future-prediction>.

Redação Onze. "Entenda os impactos e o custo da demissão de funcionários para sua empresa". **onze**. Available on: <https://www.onze.com.br/blog/custo-demissao/>
