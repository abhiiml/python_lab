# Q30. Student DataFrame with null-value handling
import pandas as pd
import numpy as np

students = {
    "roll":  ["01", "02", "03", "04", "05"],
    "name":  ["Amit", "Rhea", "Sima", "Raju", "Babita"],
    "dept":  ["CSE", "IT", np.nan, "ECE", np.nan],
    "marks": [90, np.nan, 80, 85, 95],
}

df = pd.DataFrame(students)
print("Student DataFrame:")
print(df)

# i. Find out the columns with null values
print("\ni. Columns with null values:")
print(df.columns[df.isnull().any()].tolist())
print("\nNull count per column:")
print(df.isnull().sum())

# ii. Fill the null value of Sima with CSE
df.loc[df["name"] == "Sima", "dept"] = "CSE"
print("\nii. After filling Sima's dept with CSE:")
print(df)

# iii. Delete the null value of Babita (drop her row)
df = df[~((df["name"] == "Babita") & (df["dept"].isnull()))]
print("\niii. After deleting Babita's null record:")
print(df)

# iv. Update the dept of Raju with VLSI
df.loc[df["name"] == "Raju", "dept"] = "VLSI"
print("\niv. After updating Raju's dept to VLSI:")
print(df)
