from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("dropout_model.pkl")

@app.route("/")
def home():
    return {
        "message": "Student Dropout Prediction API Running"
    }

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    student = pd.DataFrame([{
        "level": data["level"],
        "age": data["age"],
        "cgpa": data["cgpa"],
        "attendance": data["attendance"],
        "carryovers": data["carryovers"],
        "fees_paid": data["fees_paid"]
    }])

    prediction = model.predict(student)[0]

    probability = model.predict_proba(student)[0][1]

    risk = "HIGH" if prediction == 1 else "LOW"

    return jsonify({
        "risk": risk,
        "probability": round(probability * 100, 2)
    })
if __name__ == "__main__":
    app.run(debug=True)