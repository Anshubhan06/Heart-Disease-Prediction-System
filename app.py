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

    # Show Prediction Form
    if request.method == "GET":
        return render_template("predict.html")

    # Receive user inputs
    age = int(request.form["age"])
    sex = int(request.form["gender"])
    cp = int(request.form["cp"])
    trestbps = int(request.form["trestbps"])
    chol = int(request.form["chol"])
    fbs = int(request.form["fbs"])
    restecg = int(request.form["restecg"])
    thalach = int(request.form["thalach"])
    exang = int(request.form["exang"])
    oldpeak = float(request.form["oldpeak"])
    slope = int(request.form["slope"])
    ca = int(request.form["ca"])
    thal = int(request.form["thal"])

    # Create feature array
    features = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    # Prediction
    prediction = model.predict(features)[0]

    # Confidence
    confidence = np.max(model.predict_proba(features)) * 100

    # Prediction Result
    if prediction == 1:
        result = "High Risk"
        message = (
            "Your health indicators suggest an increased risk of heart disease. "
            "Please consult a qualified healthcare professional."
        )
    else:
        result = "Low Risk"
        message = (
            "Your health indicators suggest a lower likelihood of heart disease. "
            "Continue maintaining a healthy lifestyle."
        )

    # ---------------- Convert values into readable text ----------------

    gender = "Male" if sex == 1 else "Female"

    cp_types = {
        0: "Typical Angina",
        1: "Atypical Angina",
        2: "Non-Anginal Pain",
        3: "Asymptomatic"
    }

    restecg_types = {
        0: "Normal",
        1: "ST-T Wave Abnormality",
        2: "Left Ventricular Hypertrophy"
    }

    fbs_text = "Yes" if fbs == 1 else "No"

    exang_text = "Yes" if exang == 1 else "No"

    slope_types = {
        0: "Upsloping",
        1: "Flat",
        2: "Downsloping"
    }

    thal_types = {
        1: "Normal",
        2: "Fixed Defect",
        3: "Reversible Defect"
    }

    # ---------------- Dashboard ----------------

    return render_template(
        "dashboard.html",

        result=result,
        confidence=confidence,
        message=message,

        age=age,
        sex=gender,
        cp=cp_types[cp],
        trestbps=trestbps,
        chol=chol,
        fbs=fbs_text,
        restecg=restecg_types[restecg],
        thalach=thalach,
        exang=exang_text,
        oldpeak=oldpeak,
        slope=slope_types[slope],
        ca=ca,
        thal=thal_types[thal]
    )


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)