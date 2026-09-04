import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("diabetes.csv")

print("First 5 rows of the dataset:")
print(df.head())

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print("\nModel training complete!")

y_pred = model.predict(X_test)

print("\nFirst 10 predictions: ", list(y_pred[:10]))
print("First 10 actual values:", list(y_test[:10]))

accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)
print(f"That means the model got about {accuracy * 100:.2f}% of predictions correct.")