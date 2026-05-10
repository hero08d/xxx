from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load dataset
data = load_iris()
x = data.data
y = data.target

# Step 2: Create DataFrame
df = pd.DataFrame(x, columns=data.feature_names)
df['Target'] = y

# Step 3: Pairplot (IMPORTANT)
sns.pairplot(df, hue='Target')
plt.show()

# Step 4: Split data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

# Step 5: Model
model = GaussianNB()

# Step 6: Train
model.fit(xtrain, ytrain)

# Step 7: Predict
ypred = model.predict(xtest)

# Step 8: Evaluation
print("Accuracy:", accuracy_score(ytest, ypred))
print("Confusion Matrix:\n", confusion_matrix(ytest, ypred))
print("Report:\n", classification_report(ytest, ypred))

# Step 9: New sample
new_sample = [[5.1, 3.5, 1.4, 0.2]]
print("Predicted:", model.predict(new_sample))
