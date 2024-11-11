Here are **7 advanced code examples** exploring *Congruity/Incongruity*, with **clear purposes**, **strong logical relevance**, and a structured approach to achieving **great outcomes**.

---

### **Smart File Name:**  
`congruity_incongruity_modeling.py`

---

### **1. Congruity in Data Patterns**  
**Purpose:** Identify congruity in a dataset using clustering for structured alignment.  

```python
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Simulate dataset
data = np.random.rand(100, 2)

# Cluster the data
kmeans = KMeans(n_clusters=2, random_state=42)
labels = kmeans.fit_predict(data)

# Plot clusters
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='red', label='Centers')
plt.title("Congruity in Data Clustering")
plt.legend()
plt.show()
```

---

### **2. Measuring Incongruity Using Distance Metrics**  
**Purpose:** Calculate incongruity using Mahalanobis distance to detect anomalies.  

```python
import numpy as np
from scipy.spatial.distance import mahalanobis

# Simulated dataset
data = np.random.multivariate_normal([10, 5], [[1, 0.5], [0.5, 2]], 100)

# Compute Mahalanobis distance
mean = np.mean(data, axis=0)
cov = np.cov(data, rowvar=False)
inverse_cov = np.linalg.inv(cov)

distances = [mahalanobis(point, mean, inverse_cov) for point in data]
threshold = np.percentile(distances, 95)

# Detect anomalies
anomalies = [i for i, d in enumerate(distances) if d > threshold]
print(f"Detected Incongruent Points: {len(anomalies)}")
```

---

### **3. Logical Congruity Validation**  
**Purpose:** Verify logical consistency using symbolic logic.  

```python
from sympy import symbols, And, Or, Implies

# Define logical propositions
P, Q, R = symbols('P Q R')

# Define congruity: If P and Q, then R
logical_congruity = Implies(And(P, Q), R)

# Test logical congruity
print("Logical Congruity:", logical_congruity)
```

---

### **4. Congruity in Communication Analysis**  
**Purpose:** Analyze congruity between intent and sentiment in text.  

```python
from textblob import TextBlob

# Texts with intent
texts = [
    "I love this product! It's amazing.",
    "This product is okay, but not great.",
    "I hate this product! Never buying again."
]

# Check sentiment congruity
for text in texts:
    sentiment = TextBlob(text).sentiment.polarity
    congruent = sentiment > 0
    print(f"Text: '{text}' | Sentiment Polarity: {sentiment:.2f} | Congruent: {congruent}")
```

---

### **5. Modeling Congruity in Neural Networks**  
**Purpose:** Train a neural network to identify congruity in a classification problem.  

```python
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Simulate dataset
data = np.random.rand(1000, 2)
labels = (data[:, 0] + data[:, 1] > 1).astype(int)

# Build model
model = models.Sequential([
    layers.Dense(16, activation='relu', input_shape=(2,)),
    layers.Dense(8, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(data, labels, epochs=10, batch_size=32)

print("Neural Network trained to detect congruity!")
```

---

### **6. Congruity Scoring in Systems Design**  
**Purpose:** Measure congruity between system components using a scoring function.  

```python
# Component congruity scores
components = {'ComponentA': 0.9, 'ComponentB': 0.7, 'ComponentC': 0.4}

# Calculate overall congruity score
weights = {'ComponentA': 0.5, 'ComponentB': 0.3, 'ComponentC': 0.2}
overall_score = sum(components[k] * weights[k] for k in components)

print(f"Overall Congruity Score: {overall_score:.2f}")
```

---

### **7. Visualizing Incongruity in Data Distribution**  
**Purpose:** Highlight incongruity in multivariate distributions using histograms.  

```python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Simulate two distributions
group1 = np.random.normal(0, 1, 100)
group2 = np.random.normal(2, 1, 100)

# Visualize
sns.histplot(group1, color="blue", kde=True, label="Group 1")
sns.histplot(group2, color="orange", kde=True, label="Group 2")
plt.title("Incongruity in Data Distributions")
plt.legend()
plt.show()
```

---

These examples span **logical reasoning**, **data analysis**, and **machine learning** to explore and measure congruity/incongruity, offering strong relevance and structured approaches for impactful outcomes.
