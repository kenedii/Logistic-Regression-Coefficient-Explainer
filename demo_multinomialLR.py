from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression as lr
from logregcoefexplainer import explain_coefficients
from sklearn.preprocessing import StandardScaler

# Load the iris dataset
iris = load_iris()

# Scaling features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(iris.data)

# Create a logistic regression model
model = lr(max_iter=10000)

# Train the model
model.fit(X_scaled, iris.target)

print(f'Model intercept: {model.intercept_}')
print(f'Model coefficients: {model.coef_}')

explain_coefficients(model, iris.feature_names, iris.target_names)