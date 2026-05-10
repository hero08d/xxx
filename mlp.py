from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
from sklearn.decomposition import PCA
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Step 1: Load dataset
data = fetch_20newsgroups(subset='all')
X = data.data
y = data.target

# Step 2: Word cloud
text = " ".join(X[:100])
wc = WordCloud().generate(text)
plt.imshow(wc)
plt.axis("off")
plt.show()

# Step 3: Convert text → numbers
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

# Step 4: Split data
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2)

# Step 5: Model
model = MLPClassifier()
model.fit(X_train, y_train)

# Step 6: Predict
y_pred = model.predict(X_test)

# Step 7: Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='weighted'))
print("Recall:", recall_score(y_test, y_pred, average='weighted'))
print(classification_report(y_test, y_pred))

# Step 8: PCA visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_tfidf.toarray())
plt.scatter(X_pca[:,0], X_pca[:,1], c=y)
plt.show()
