# Q31. Titanic dataset (download train.csv from Kaggle and save as titanic.csv)
import pandas as pd

AGE_LIMIT = 30   # <-- change to the age written in your question

df = pd.read_csv("titanic.csv")
print("Original shape:", df.shape)

# i. Clean the dataset and print the resultant dataset
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df = df.drop(columns=["Cabin"])          # mostly null, so drop it
print("\ni. Cleaned dataset:")
print(df)
print("\nRemaining nulls:\n", df.isnull().sum())

# ii. Details of passengers whose age is more than AGE_LIMIT and are female
print(f"\nii. Female passengers older than {AGE_LIMIT}:")
print(df[(df["Age"] > AGE_LIMIT) & (df["Sex"] == "female")])

# iii. Describe the dataset for passengers of class 1
print("\niii. Describe for Pclass 1:")
print(df[df["Pclass"] == 1].describe())

# iv. Remove duplicate values in PassengerId
df = df.drop_duplicates(subset="PassengerId")
print("\niv. Shape after removing duplicate PassengerId:", df.shape)

# v. Insert a column in the dataset
df.insert(2, "Family_Size", df["SibSp"] + df["Parch"] + 1)
print("\nv. After inserting 'Family_Size' column:")
print(df.head())

df.to_csv("titanic_cleaned.csv", index=False)
