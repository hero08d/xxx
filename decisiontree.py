from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load dataset
data = load_diabetes()
x = data.data
y = data.target

# Step 2: Convert to binary (IMPORTANT)
y = [1 if i >= np.mean(y) else 0 for i in y]

# Step 3: Split data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3)

# Step 4: Create model (ID3 uses entropy)
model = DecisionTreeClassifier(criterion='entropy')

# Step 5: Train
model.fit(xtrain, ytrain)

# Step 6: Predict
ypred = model.predict(xtest)

# Step 7: Accuracy
print("Accuracy:", accuracy_score(ytest, ypred))

# Step 8: Plot tree
plot_tree(model, feature_names=data.feature_names, filled=True)
plt.show()

# Step 9: Print rules
print(export_text(model, feature_names=data.feature_names))
