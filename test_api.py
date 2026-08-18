import requests

data = {
    "faculty": 0,
    "department": 0,
    "level": 300,
    "gender": 0,
    "age": 22,
    "cgpa": 1.8,
    "attendance": 40,
    "carryovers": 5,
    "fees_paid": 0
}

response = requests.post(
    "https://ai-model-prediction.onrender.com/predict",
    json=data
)

print(response.json())