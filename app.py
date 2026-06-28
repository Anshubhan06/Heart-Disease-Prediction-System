from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model/heart_disease_model.pkl")

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Heart Risk Check Page
@app.route("/predict")
def predict():
    return render_template("predict.html")

# BMI Calculator
@app.route("/bmi")
def bmi():
    return render_template("bmi.html")

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)