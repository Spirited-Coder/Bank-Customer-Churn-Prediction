# Bank Customer Churn Prediction

This project is a Flask web application designed to predict bank customer churn. It includes user authentication and a machine learning model for churn prediction.

## Features

- User Registration
- User Login
- Churn Prediction
- Responsive Design

## Screenshots

### Login Page
![Login Page](./screenshots/login_page.png)

### Registration Page
![Registration Page](./screenshots/register_page.png)

### Prediction Page
![Prediction Page](./screenshots/predict_page.png)

## Installation

### Prerequisites

- Python 3.x
- Virtual Environment (recommended)

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
- `static/`: Directory containing the css files and images.
- `screenshots/`: Directory containing the screenshots of the website.
- `templates/`: Directory containing the templates.
- `src/`: Source code for data preprocessing, feature engineering, model building, and evaluation.
- `models/`: Directory for saving trained models.
- `script.py/`: File containing the main Flask application.
- `userdb.py/`: File where the database was created.
- `requirements.text/`: File where the requirements are mentioned.
- `reports/`: Generated reports and visualizations from the analysis.
- `README.md`: Project overview and instructions.

## Steps to Run the Project
1. **Clone the Repository**
   ```
   git clone https://github.com/yourusername/bank-customer-churn-prediction.git
   cd bank-customer-churn-prediction
   
2. **Create and Activate a virtual environment**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. **Install the required dependencies**
   ```
   pip install -r requirements.txt
   
4. **Initialize the database**
   ```
   python db_create.py
   
5. **Run the application**
   ```
   python app.py

## Usage
Open your web browser and navigate to http://localhost:5000.
### User Registration
- Navigate to the registration page.
- Fill in your details and submit the form to create a new account.
### User Login
- Navigate to the login page.
- Enter your email and password to log in.
### Churn Prediction
- Once logged in, navigate to the prediction page.
- Enter the required customer information to predict whether the customer will churn.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements
<ul>
    <li>Kaggle for providing the dataset</li>
    <li>Scikit-learn, pandas, and matplotlib for their powerful data science libraries</li>
</ul>
