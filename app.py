# app.py
from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

app = Flask(__name__)

# Load pre-trained models
clf_decision_tree = joblib.load("decision_tree_model.pkl")
clf_svc = joblib.load("svc_model.pkl")

# Function to preprocess input data
def preprocess_input(data):
    scaler = StandardScaler()
    return scaler.fit_transform(data)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission and show predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input data from the form
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        # Preprocess input data
        input_data = pd.DataFrame({
            'age': [age], 'sex': [sex], 'cp': [cp], 'trestbps': [trestbps], 'chol': [chol],
            'fbs': [fbs], 'restecg': [restecg], 'thalach': [thalach], 'exang': [exang], 'oldpeak': [oldpeak],
            'slope': [slope], 'ca': [ca], 'thal': [thal]
        })
        input_data = preprocess_input(input_data)

        # Get predictions from both models
        dt_prediction = clf_decision_tree.predict(input_data)
        svc_prediction = clf_svc.predict(input_data)

        # Render predictions on the result page
        return render_template('result.html', dt_prediction=dt_prediction[0], svc_prediction=svc_prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
