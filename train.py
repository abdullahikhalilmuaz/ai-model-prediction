import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("student_dropout_dataset.csv")

# Features used for prediction
X = df[
    [
        "level",
        "age",
        "cgpa",
        "attendance",
        "carryovers",
        "fees_paid"
    ]
]

# Target
y = df["dropout"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", round(accuracy * 100, 2), "%")

# Save model
joblib.dump(model, "dropout_model.pkl")

print("Model saved successfully!")