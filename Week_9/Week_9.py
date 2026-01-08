
# # Week No.9 The Developers Arena Internship Task

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

path = r"C:\Users\subha\Desktop\Devlopers-Arena-Internship\Datasets\house_prices.csv"

# Load the dataset
df = pd.read_csv(path)

df.head()

df.tail()

df.isnull().sum() # checking the missing values in the dataset

df.duplicated().sum() # checking the duplicate values

# --- 1. Exploratory Data Analysis (EDA) ---

# Distribution of Target Variable (Price)
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], kde=True, color='blue')
plt.title('Distribution of House Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')

# Relationship: Area vs Price
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Area', y='Price', hue='Location')
plt.title('Area vs Price by Location')
plt.savefig('area_vs_price.png')

# Relationship: Property Type vs Price
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Property_Type', y='Price')
plt.title('Property Type vs Price')

# Correlation Matrix (Numerical only)
plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')

# --- 2. Data Preprocessing & Model Training ---

# Define Features and Target
X = df.drop(['Property_ID', 'Price'], axis=1)
y = df['Price']


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define categorical and numerical features
categorical_features = ['Location', 'Property_Type']
numerical_features = ['Area', 'Bedrooms', 'Bathrooms', 'Age']

# Preprocessing: OneHotEncode categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_features)
    ],
    remainder='passthrough'
)


# Create a pipeline with preprocessing and model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train the model
model.fit(X_train, y_train)

# --- 3. Predictions and Evaluation ---

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae:,.2f}")
print(f"Mean Squared Error (MSE): {mse:,.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:,.2f}")
print(f"R2 Score: {r2:.4f}")

# --- 4. Visualize Results ---

# Actual vs Predicted
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='green')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted House Prices')

# Residual Plot
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True, color='purple')
plt.title('Distribution of Residuals')
plt.xlabel('Residual (Error)')




