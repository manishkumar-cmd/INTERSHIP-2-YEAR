import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Sample dataset (You should replace it with a real dataset)
data = pd.DataFrame({
    'brand': ['Hero', 'Honda', 'Yamaha', 'Bajaj'],
    'year': [2015, 2016, 2014, 2018],
    'kms_driven': [30000, 40000, 25000, 10000],
    'price': [35000, 40000, 30000, 50000]
})

# Convert categorical to numeric
data['brand'] = data['brand'].astype('category').cat.codes

X = data[['brand', 'year', 'kms_driven']]
y = data['price']

model = RandomForestRegressor()
model.fit(X, y)

# Save the model
pickle.dump(model, open('model.pkl', 'wb'))
