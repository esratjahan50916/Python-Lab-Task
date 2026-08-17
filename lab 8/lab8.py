# Problem - 1

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

s = pd.Series(calories)
print(s)

total = s.sum()
print("Total calories:", total)
print("\n")


# Problem - 2

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)

selected_rows = df.loc[[0, 2]]
print(selected_rows)
print("\n")

# Problem - 3

df = pd.read_csv("./deceptive-opinion.csv")

print(df.head())
print(df.tail())
print(df.info())
print("\n")

# Problem - 4


import seaborn as sns

titanic = sns.load_dataset("titanic")
print(titanic.head())

print(titanic.isnull().sum())

titanic["age"] = titanic["age"].fillna(titanic["age"].mean())

titanic["fare"] = titanic["fare"].astype(float)

titanic = titanic.drop_duplicates()

titanic["sex"] = titanic["sex"].str.lower()

print(titanic.info())