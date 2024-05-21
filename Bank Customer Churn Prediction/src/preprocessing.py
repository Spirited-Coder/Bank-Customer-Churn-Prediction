{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2ae4dd8b-7ebd-4f6f-b438-c77a7ae9f577",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\chakr\\AppData\\Local\\Temp\\ipykernel_3192\\4080736814.py:1: DeprecationWarning: \n",
      "Pyarrow will become a required dependency of pandas in the next major release of pandas (pandas 3.0),\n",
      "(to allow more performant data types, such as the Arrow string type, and better interoperability with other libraries)\n",
      "but was not found to be installed on your system.\n",
      "If this would cause problems for you,\n",
      "please provide us feedback at https://github.com/pandas-dev/pandas/issues/54466\n",
      "        \n",
      "  import pandas as pd\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "83bd3779-e51d-4584-85c1-2453c68969fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def preprocessing_data(input_path, output_path):\n",
    "    data = pd.read_csv(input_path)\n",
    "    data = data.dropna(axis=1)\n",
    "    data = data.drop(columns=['Surname', 'RowNumber', 'CustomerId'])\n",
    "    data = pd.get_dummies(data, columns=['Geography', 'Gender'], drop_first=True)\n",
    "    data.to_csv(output_path, index=False)\n",
    "if __name__==\"__main__\":\n",
    "    preprocessing_data('..\\\\data\\\\Churn_Modelling.csv', '..\\\\data\\\\preprocessed_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f36c50ff-6834-46fb-86e7-147c4a95084c",
   "metadata": {},
   "outputs": [],
   "source": []
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
