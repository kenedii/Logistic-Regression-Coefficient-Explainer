from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression as lr
from logregcoefexplainer import explain_coefficients
from sklearn.preprocessing import StandardScaler

# Load the iris dataset
bc = load_breast_cancer()

# Scaling features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(bc.data)

# Create a logistic regression model
model = lr(max_iter=10000)

# Train the model
model.fit(X_scaled, bc.target)

explain_coefficients(model, bc.feature_names, bc.target_names[0])
