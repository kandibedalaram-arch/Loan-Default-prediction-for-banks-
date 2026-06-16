# Loan Default Prediction for Banks

## 📌 Project Overview

This project focuses on predicting loan default risk for a digital lending fintech company using a dataset of 255,347 loan records. The objective is to build a machine learning framework that helps financial institutions make data-driven lending decisions and reduce credit risk.

The analysis identifies key risk drivers such as income level, interest rate, credit score, and employment status, and builds predictive models to estimate the probability of loan default.

---

## 🎯 Business Objective

The primary goal of this project is to:

* Improve loan approval decision-making using predictive analytics
* Minimize financial losses due to loan defaults
* Identify high-risk applicants early in the lending process
* Support data-driven credit risk policies

---

## 🧠 Key Insights

* High interest rates, low income, and unemployment are major risk indicators for loan default.
* Default probability varies significantly across employment type, credit score, and debt-to-income ratio.
* Model-based risk scoring can improve lending decisions and reduce non-performing loans.

---

## 📊 Dataset Information

* **Source:** Kaggle Loan Default Dataset
* **URL:** https://www.kaggle.com/datasets/nikhil1e9/loan-default
* **Size:** 255,347 rows × 18 columns
* **Target Variable:** Default (0 = No Default, 1 = Default)
* **Default Rate:** ~12% (imbalanced dataset)

### Key Features:

Age, Income, LoanAmount, InterestRate, CreditScore, MonthsEmployed, NumCreditLines, DTIRatio, Education, EmploymentType, MaritalStatus, HasMortgage, HasDependents, LoanPurpose, HasCoSigner

---

## ⚙️ Methodology

### 1. Exploratory Data Analysis (EDA)

* Analyzed relationships between default rate and key financial variables
* Identified patterns across income, credit score, employment status, and loan characteristics

### 2. Data Preprocessing

* Handled missing values and data inconsistencies
* Encoded categorical variables
* Addressed class imbalance

### 3. Feature Engineering

* Created meaningful features to improve model performance
* Selected important predictors based on statistical and business relevance

### 4. Machine Learning Models

* Logistic Regression
* Random Forest
* Gradient Boosting
* LinearSVC

  
### 5. Model Evaluation

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC
* ROC Curve

Logistic Regression and Linear SVC performed best with the optimal balance of Recall,F1Score and ROC-AUC.

---

## 🔍 Model Explainability

* Applied Feature Importance techniques to identify key predictors of loan default
* Used SHAP analysis to interpret model predictions and understand feature impact

---

## 📈 Key Results
* Identified top risk factors:

  * Income
  * Interest Rate
  * Credit Score
  * Employment Status
* Developed a risk scoring approach to support lending decisions

---

## 💡 Business Recommendations

* Implement predictive risk scoring for loan approval processes
* Use conservative thresholds for high-risk applicant identification
* Offer co-signer or collateral-based policies for risky profiles
* Optimize interest rates based on predicted default probability

---

## 🚀 Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Seaborn

---

## 📌 Conclusion

This project demonstrates how machine learning can be applied to credit risk analysis to improve lending decisions, reduce financial losses, and support data-driven banking strategies.
