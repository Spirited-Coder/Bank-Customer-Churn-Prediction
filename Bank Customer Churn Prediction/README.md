# Bank Customer Churn Prediction

## Project Overview
This repository contains a machine learning project aimed at predicting whether a bank customer will churn, i.e., leave the bank. Using a dataset obtained from Kaggle, the project leverages various data preprocessing techniques, exploratory data analysis, feature engineering, and machine learning algorithms to build an effective churn prediction model.

## Dataset
The dataset used in this project is sourced from Kaggle's "Bank Customer Churn Prediction" competition. It contains customer information and various features that can be used to predict churn.

### Dataset Description
- **RowNumber**: Unique identifier for each row (removed during preprocessing)
- **CustomerId**: Unique identifier for each customer
- **Surname**: Customer's surname (removed during preprocessing)
- **CreditScore**: Customer's credit score
- **Geography**: Country of the customer
- **Gender**: Customer's gender
- **Age**: Customer's age
- **Tenure**: Number of years the customer has been with the bank
- **Balance**: Customer's account balance
- **NumOfProducts**: Number of bank products the customer uses
- **HasCrCard**: Whether the customer has a credit card (binary: 1 if yes, 0 if no)
- **IsActiveMember**: Whether the customer is an active member (binary: 1 if yes, 0 if no)
- **EstimatedSalary**: Customer's estimated salary
- **Exited**: Whether the customer has left the bank (target variable: 1 if yes, 0 if no)

## Project Structure
The repository is organized as follows:

- `data/`: Directory containing the dataset.
- `notebooks/`: Jupyter notebooks for exploratory data analysis, model training, and evaluation.
- `src/`: Source code for data preprocessing, feature engineering, model building, and evaluation.
- `models/`: Directory for saving trained models.
- `reports/`: Generated reports and visualizations from the analysis.
- `README.md`: Project overview and instructions.

## Steps to Run the Project
1. **Clone the Repository**
   ```
   git clone https://github.com/yourusername/bank-customer-churn-prediction.git
   cd bank-customer-churn-prediction```
2. **Install Dependencies**
   Ensure you have Python and pip installed. Then, install the required packages.
   ```
   pip install -r requirements.txt```
3. **Preprocess Data**
   Run the preprocessing script to clean and transform the data
   ```
   python src/preprocess_data.py```
4. **Run Jupyter Notebook**
   Start Jupyter Notebook and open the notebooks in the notebooks/ directory to explore data, train models, and evaluate performance.
5. **Train the Model**
   Run the model training script
   ```
   python src/train_model.py```
6. **Evaluate the Model**
   Run the evaluation script to get performance metrics and plots.
   ```
   python src/evaluate_model.py```
   
## Features and Techniques
**Data Preprocessing**
<ul>
    <li>Handling Missing Values</li>
    <li>Dropping Irrelevant Columns</li>
    <li>Converting categorical features to numerical values using one-hot encoding</li>
</ul>

**Exploratory Data Analysis**
<ul>
    <li>Visualizing distributions of features</li>
    <li>Identifying correlations between features and the target variable</li>
    <li>Detecting outliers and anomalies</li>
</ul>

**Feature Engineering**
<ul>
    <li>Creating new features based on domain knowledge</li>
    <li>Scaling numerical features</li>
    <li>Encoding categorical features</li>
</ul>

**Model Building**
<ul>
    <li>Training various machine learning models (e.g., Logistic Regression, Decision Trees, Random Forests, Gradient Boosting)</li>
    <li>Hyperparameter tuning using Grid Search and Random Search</li>
    <li>Evaluating model performance using cross-validation</li>
</ul>

**Model Evaluation**
<ul>
    <li>Confusion matrix, classification report (precision, recall, F1-score)</li>
    <li>ROC curve and AUC score</li>
    <li>Precision-Recall curve</li>
</ul>

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
<ul>
    <li>Kaggle for providing the dataset</li>
    <li>Scikit-learn, pandas, and matplotlib for their powerful data science libraries</li>
</ul>