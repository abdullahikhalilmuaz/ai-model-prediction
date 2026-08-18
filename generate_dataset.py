import pandas as pd
import random

faculties = {
    "Science": ["Computer Science", "Mathematics", "Biology", "Chemistry"],
    "Education": ["Education Biology", "Education Mathematics"],
    "Arts": ["History", "English"],
    "Social Sciences": ["Economics", "Political Science"],
    "Management Sciences": ["Accounting", "Business Administration"]
}

students = []

for i in range(1, 3001):

    faculty = random.choice(list(faculties.keys()))
    department = random.choice(faculties[faculty])

    cgpa = round(random.uniform(0.5, 5.0), 2)
    attendance = random.randint(20, 100)
    carryovers = random.randint(0, 8)
    fees_paid = random.choice([0, 1])

    risk_score = 0

    if cgpa < 2.0:
        risk_score += 3

    if attendance < 50:
        risk_score += 3

    if carryovers > 3:
        risk_score += 2

    if fees_paid == 0:
        risk_score += 2

    dropout = 1 if risk_score >= 5 else 0

    students.append({
        "student_id": f"STD{i:04}",
        "faculty": faculty,
        "department": department,
        "level": random.choice([100, 200, 300, 400]),
        "gender": random.choice(["M", "F"]),
        "age": random.randint(17, 30),
        "cgpa": cgpa,
        "attendance": attendance,
        "carryovers": carryovers,
        "fees_paid": fees_paid,
        "dropout": dropout
    })

df = pd.DataFrame(students)

df.to_csv("student_dropout_dataset.csv", index=False)

print("Dataset generated successfully!")
print("Total students:", len(df))