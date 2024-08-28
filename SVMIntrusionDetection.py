from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd

# Example: Load a sample dataset for intrusion detection (Replace with real IDS dataset)
# Load dataset from sklearn or use a custom dataset with network features
X, y = datasets.make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create an SVM model with a Gaussian (RBF) kernel
svm_model = SVC(kernel='rbf', C=1, gamma=0.1)

# Train the SVM model
svm_model.fit(X_train, y_train)

# Predict on test data
y_pred = svm_model.predict(X_test)

# Evaluate the model
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
