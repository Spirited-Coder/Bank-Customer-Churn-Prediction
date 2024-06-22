# script.py
from flask import *
import joblib
import sqlite3
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

model1 = joblib.load('models/trained_model.pkl')   

DATABASE = 'users.db'

def get_db():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    return con

@app.route('/')
def home():
    if 'loggedin' in session:
        return render_template('home.html')
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        try:
            with get_db() as con:
                cursor = con.cursor()
                cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
                account = cursor.fetchone()
                if account:
                    session['loggedin'] = True
                    session['id'] = account['id']
                    session['username'] = account['username']
                    msg = 'Logged in Successfully'
                    return render_template('home.html', msg=msg)
                else:
                    msg = 'Incorrect Username/Password'
        except Exception as e:
            msg = f'Error in Login: {str(e)}'
            app.logger.error(msg)
    return render_template('login.html', msg=msg)

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        try:
            with get_db() as con:
                cursor = con.cursor()
                cursor.execute('SELECT * FROM users WHERE username=?', (username,))
                account = cursor.fetchone()
                if account:
                    msg = 'Account already exists'
                elif not re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', email):
                    msg = 'Invalid email address!'
                elif not re.match(r'^[A-Za-z0-9]+$', username):
                    msg = 'Username must contain only characters and numbers!'
                elif not username or not password or not email:
                    msg = 'Please fill out the form!'
                else:
                    cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
                    con.commit()
                    msg = 'User successfully added!'
                    return redirect(url_for('login'))
        except Exception as e:
            msg = f'Error in registration: {str(e)}'
            app.logger.error(msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form'
    return render_template('registration.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/predict_churn', methods=['POST'])
def predict_churn():
    try:
        data = request.get_json()
        if 'features' in data:
            features = data['features']
            # Convert features to float if necessary (ensure all values are numeric)
            features = [float(f) for f in features]
            
            # Perform prediction
            prediction = model1.predict([features])[0]  # Assuming model1 predicts directly
            result = "Positive" if prediction == 1 else "Negative"
            
            return jsonify({'prediction': result})
        else:
            return jsonify({'error': 'Invalid JSON format'})
    except Exception as e:
        msg = f'Error in prediction: {str(e)}'
        app.logger.error(msg)
        return jsonify({'error': 'Prediction failed'})


if __name__ == '__main__':
    app.run(debug=True)
