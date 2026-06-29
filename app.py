from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained Machine Learning model
model = joblib.load("model/heart_disease_model.pkl")

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- ABOUT ----------------
@app.route("/about")
def about():
    return render_template("about.html")

# ---------------- BMI ----------------
@app.route("/bmi")
def bmi():
    return render_template("bmi.html")

# ---------------- CONTACT ----------------
@app.route("/contact")
def contact():
    return render_template("contact.html")

# ---------------- PREDICT ----------------
@app.route("/predict", methods=["GET", "POST"])
def predict():

    # Open Prediction Page
    if request.method == "GET":
        return render_template("predict.html")

    # Tomorrow we'll receive all 13 features here
    # Example:
    # age = int(request.form["age"])

    # We'll preprocess the data,
    # send it to the model,
    # and display the dashboard.

    return render_template("dashboard.html")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)