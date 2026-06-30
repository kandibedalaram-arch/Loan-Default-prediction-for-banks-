Loan Default Prediction for Banks

Project Overview

This project predicts loan default risk using machine learning to help financial institutions make informed lending decisions and reduce credit risk. A dataset containing 255,347 loan records was analyzed to identify key factors influencing loan defaults and build predictive models for risk assessment.

The final solution includes an end-to-end machine learning pipeline, REST API development using FastAPI, containerization with Docker, and deployment on AWS EC2.

Business Objective

The objectives of this project are to:

* Predict whether a customer is likely to default on a loan.
* Identify high-risk applicants before loan approval.
* Support data-driven credit risk assessment.
* Reduce financial losses caused by loan defaults.

Dataset Information

* Source: Kaggle – Loan Default Dataset
* Size: 255,347 records × 18 features
* Target Variable: Default (0 = No Default, 1 = Default)

Features

* Age
* Income
* Loan Amount
* Interest Rate
* Credit Score
* Months Employed
* Number of Credit Lines
* Debt-to-Income Ratio
* Education
* Employment Type
* Marital Status
* Mortgage Status
* Dependents
* Loan Purpose
* Co-signer Status

Project Workflow

1. Data Preprocessing

* Cleaned and prepared the dataset
* Encoded categorical variables
* Handled class imbalance
* Performed feature engineering

2. Exploratory Data Analysis (EDA)

* Analyzed customer demographics and financial characteristics
* Identified relationships between loan defaults and key variables
* Visualized important trends affecting default risk

3. Machine Learning Models

The following classification algorithms were trained and compared:

* Logistic Regression
* Random Forest
* Gradient Boosting
* Linear SVC

4. Model Evaluation

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC
* ROC Curve

Logistic Regression and Linear SVC achieved the best balance between Recall, F1-Score, and ROC-AUC, making them the most suitable models for identifying high-risk loan applicants.


Key Insights

* Low income increases the likelihood of loan default.
* Higher interest rates are associated with increased default risk.
* Customers with lower credit scores are more likely to default.
* Employment status significantly impacts repayment behavior.

Business Recommendations

* Implement machine learning-based risk scoring during loan approval.
* Review high-risk applications before approval.
* Offer additional verification or co-signer requirements for risky applicants.
* Use predictive analytics to improve lending strategies and reduce non-performing loans.

Model Deployment

The trained machine learning model was deployed as a REST API to enable real-time predictions.

Deployment Workflow

* Developed REST API endpoints using FastAPI.
* Implemented request validation using Pydantic.
* Tested API endpoints using Postman.
* Containerized the application using Docker.
* Deployed the Dockerized application on AWS EC2.
* Managed version control using Git and GitHub.

The deployed API accepts applicant details as input and returns a prediction indicating whether the customer is likely to default on the loan.

Tools & Technologies

Programming & Analysis

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

API Development

* FastAPI
* Pydantic
* Postman

Deployment

* Docker
* AWS EC2

Version Control

* Git
* GitHub

Future Improvements

* Improve model performance using XGBoost or LightGBM.
* Implement model monitoring and logging.
* Automate deployment using CI/CD pipelines.
* Deploy using scalable cloud services such as AWS ECS or Kubernetes.

 Conclusion

This project demonstrates an end-to-end machine learning workflow, from data preprocessing and predictive modeling to API development and cloud deployment. It highlights the practical application of machine learning, FastAPI, Docker, and AWS EC2 to build scalable solutions for real-world credit risk assessment.

Author

[Your Name]

* LinkedIn: Add your LinkedIn profile
* GitHub: Add your GitHub profile
