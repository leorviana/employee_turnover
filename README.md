# Employee Turnover

# Business Problem

<b>The data below, as well as its context, is completely fictitious.</b>

In a meeting with the human resources team of the company we work for, we were informed that many employees leave the company after two years. 

It was reported that the cost of leaving one employee and hiring another is approximately $4100.00. In addition, we lose productivity in the periods between the departure of an employee and the entry of another

Our goal is then to help identify employees who are most likely to leave the company. The thought solution was to develop a probability estimation model.

<p align="center">
  <img src="https://www.cleanlink.com/resources/editorial/2021/employees-26883.png">
</p>

# Project planning

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

- Data preprocessing (OneHotEncoding, normalization, imbalanced data);
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
    <li><a href="https://www.spyder-ide.org/">Spyder IDE</a></li>
    <li><a href="https://powerbi.microsoft.com/pt-br/">Microsoft Power BI</a></li>
  </ul>
 </p>
 
# Analysis and Conclusion Report
The purpose of the report below is to further assist stakeholders with a little more in-depth analysis of certain details and phenomena observed.

<p align="left">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/rh_report_page-0001.jpg">
</p>
________________________________________________________________________________________________________________________________________________________
<p align="left">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/rh_report_page-0002.jpg">
</p>
________________________________________________________________________________________________________________________________________________________
<p align="left">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/rh_report_page-0003.jpg">
</p>
________________________________________________________________________________________________________________________________________________________
<p align="left">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/rh_report_page-0004.jpg">
</p>
________________________________________________________________________________________________________________________________________________________
<p align="left">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/rh_report_page-0005.jpg">
</p>
________________________________________________________________________________________________________________________________________________________
<p align="left">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/rh_report_page-0006.jpg">
</p>


# Model Deployment

<p align="center">
  <img src="https://github.com/leorviana/employee_turnover/blob/main/images/deploy_image.png">
</p>

You can access the web app developed to provide the model and use it through the link: 
<https://share.streamlit.io/leorviana/employee_turnover/main/app.py>.

# Business Evaluation
The average cost of terminating and hiring a new employee to replace is $4100.00
With this model we were able to identify employees who are about to leave and try to recover them before then leave.

As we can see, our model can identify correctly 75% of the employees that will turnover in the future. If we consider that we can retain only 40% of the employees that our model identify, our model can reduce the  loss of employees from 30%. Saving $82410.00 per month.

# Conclusion
At the end of this project it was possible to reach a very good number for reducing the spending of human resources company sector, the human resources manager now has in hand which characteristics a employee that will left the company has and a model that predict if a specific employee will turnover, being thus it is correct to say that the main objective of this project was successfully achieved.

# Next steps
To further improve the model and generate more accurate predictions, we may collect more data and seek to identify other employee characteristics.

# References

Employee Future Prediction. Kaggle. Available on: <https://www.kaggle.com/tejashvi14/employee-future-prediction>.

Redação Onze. "Entenda os impactos e o custo da demissão de funcionários para sua empresa". **onze**. Available on: <https://www.onze.com.br/blog/custo-demissao/>
