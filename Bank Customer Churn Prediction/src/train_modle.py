{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c761b86d-8dde-4363-ad41-f8ebcf4e8470",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\chakr\\AppData\\Local\\Temp\\ipykernel_5092\\2596302087.py:1: DeprecationWarning: \n",
      "Pyarrow will become a required dependency of pandas in the next major release of pandas (pandas 3.0),\n",
      "(to allow more performant data types, such as the Arrow string type, and better interoperability with other libraries)\n",
      "but was not found to be installed on your system.\n",
      "If this would cause problems for you,\n",
      "please provide us feedback at https://github.com/pandas-dev/pandas/issues/54466\n",
      "        \n",
      "  import pandas as pd\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model training complete and performance report saved.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import classification_report\n",
    "import joblib\n",
    "\n",
    "data = pd.read_csv('../data/preprocessed_data.csv')\n",
    "\n",
    "X = data.drop('Exited', axis=1)\n",
    "y = data['Exited']\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "model = RandomForestClassifier(random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "joblib.dump(model, '../models/trained_model.pkl')\n",
    "\n",
    "y_pred = model.predict(X_test)\n",
    "report = classification_report(y_test, y_pred)\n",
    "with open('../reports/model_performance.txt', 'w') as f:\n",
    "    f.write(report)\n",
    "print(\"Model training complete and performance report saved.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
