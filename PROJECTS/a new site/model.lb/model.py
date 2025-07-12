# model_creator.py

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib

# Step 1: Load sample data
X, y = load_iris(return_X_y=True)

# Step 2: Train a simple model
model = DecisionTreeClassifier()
model.fit(X, y)

# Step 3: Save model as 'model.lb'
joblib.dump(model, 'model.lb')

print("Model saved as model.lb")
