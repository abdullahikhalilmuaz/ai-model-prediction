import pandas as pd
import joblib

model = joblib.load("dropout_model.pkl")

student = pd.DataFrame([{
    "level": 300,
    "age": 22,
    "cgpa": 1.8,
    "attendance": 40,
    "carryovers": 5,
    "fees_paid": 0
}])

prediction = model.predict(student)
probability = model.predict_proba(student)

print("Prediction:", prediction[0])

print(
    "Dropout Risk:",
    round(probability[0][1] * 100, 2),
    "%"
)