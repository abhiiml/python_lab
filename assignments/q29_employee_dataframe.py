# Q29. Create a DataFrame from a dictionary for 5 employees
import pandas as pd

employees = {
    "emp_id":   ["E01", "E02", "E03", "E04", "E05"],
    "emp_name": ["Amit", "Suraj", "Alia", "Sonal", "Ira"],
    "dept":     ["IT", "DS", "AI", "IT", "DS"],
    "salary":   [10000, 15000, 18000, 14000, 16000],
}

df = pd.DataFrame(employees)
print("Employee DataFrame:")
print(df)

# 1. Print the records of first 2 employees
print("\n1. First 2 employees:")
print(df.head(2))

# 2. Print the records of last 2 employees
print("\n2. Last 2 employees:")
print(df.tail(2))

# 3. Print the record having maximum salary
print("\n3. Record with maximum salary:")
print(df[df["salary"] == df["salary"].max()])
