import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.tree import DecisionTreeClassifier

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("student_dropout_dataset.csv")

# Convert text columns
df["gender"] = df["gender"].map({"M": 0, "F": 1})

df["faculty"] = df["faculty"].astype("category").cat.codes

df["department"] = df["department"].astype("category").cat.codes

# Features
X = df.drop(["student_id", "dropout"], axis=1)

# Target
y = df["dropout"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

models = {
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Logistic Regression": LogisticRegression(
        max_iter=1000
    )
}

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"{name}: {round(accuracy * 100, 2)}%")