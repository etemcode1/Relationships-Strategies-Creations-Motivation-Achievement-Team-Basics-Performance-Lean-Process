### **Generativity Versus Stagnation: Advanced Code Examples**  
These examples focus on creating systems and models that reflect the concept of **generativity versus stagnation**—encouraging growth, purpose, and community contribution while avoiding stagnation, both at personal and systemic levels.

---

### **Smart File Name:**  
`generativity_vs_stagnation_models.py`

---

### **1. Generativity Growth Model with Logistic Function**  
Simulating growth and its constraints to model generativity versus stagnation.  
```python
import numpy as np
import matplotlib.pyplot as plt

def logistic_growth_model(initial_population, carrying_capacity, growth_rate, time_steps):
    """
    Logistic growth model simulating generativity as bounded growth, constrained by carrying capacity.
    """
    population = [initial_population]
    for _ in range(1, time_steps):
        next_population = population[-1] + growth_rate * population[-1] * (1 - population[-1] / carrying_capacity)
        population.append(next_population)
    return population

# Parameters
initial_population = 10
carrying_capacity = 500
growth_rate = 0.1
time_steps = 100

population_over_time = logistic_growth_model(initial_population, carrying_capacity, growth_rate, time_steps)

# Plot
plt.plot(population_over_time)
plt.title("Generativity Growth Model")
plt.xlabel("Time Steps")
plt.ylabel("Population (Generativity)")
plt.show()
```

---

### **2. Decision Tree for Generativity or Stagnation**  
A decision-making model based on conditions that lead to either generativity or stagnation.  
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

def decision_tree_model(features, labels):
    """
    Train a decision tree classifier to determine conditions leading to generativity or stagnation.
    """
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
    clf.fit(features, labels)
    return clf

# Features: [community engagement, personal growth, mentorship hours]
# Labels: 1 (Generativity), 0 (Stagnation)
features = [[10, 7, 5], [5, 3, 1], [8, 9, 6], [1, 2, 0], [6, 5, 3]]
labels = [1, 0, 1, 0, 1]

clf = decision_tree_model(features, labels)

# Visualize the tree
plt.figure(figsize=(10, 6))
tree.plot_tree(clf, feature_names=["Engagement", "Growth", "Mentorship"], class_names=["Stagnation", "Generativity"], filled=True)
plt.title("Decision Tree: Generativity vs. Stagnation")
plt.show()
```

---

### **3. Generativity Network Simulation with Node Contribution**  
Simulating a network of individuals where generativity is modeled by contributions to a larger system.  
```python
import networkx as nx

def generativity_network(num_nodes, contribution_factor):
    """
    Create a network where nodes represent individuals and edges represent contributions to generativity.
    """
    G = nx.erdos_renyi_graph(num_nodes, contribution_factor)
    nx.set_node_attributes(G, {i: np.random.randint(1, 10) for i in G.nodes()}, "contribution")
    return G

# Parameters
num_nodes = 15
contribution_factor = 0.3

G = generativity_network(num_nodes, contribution_factor)

# Visualize the network with contributions
node_sizes = [100 * G.nodes[node]["contribution"] for node in G.nodes()]
nx.draw(G, with_labels=True, node_size=node_sizes, node_color="skyblue", font_size=10)
plt.title("Generativity Network")
plt.show()
```

---

### **4. Predicting Stagnation Using Time Series Models**  
Using ARIMA for forecasting stagnation or generativity trends.  
```python
from statsmodels.tsa.arima.model import ARIMA

def predict_stagnation_trend(data, forecast_steps):
    """
    Predict stagnation or generativity trends using ARIMA time series forecasting.
    """
    model = ARIMA(data, order=(1, 1, 1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=forecast_steps)
    return forecast

# Sample generativity trend data (past contributions over time)
data = [10, 15, 13, 17, 19, 18, 22, 24, 23, 30]

forecast_steps = 5
forecasted_trend = predict_stagnation_trend(data, forecast_steps)

# Plot
plt.plot(range(len(data)), data, label="Past Data")
plt.plot(range(len(data), len(data) + forecast_steps), forecasted_trend, label="Forecast", linestyle="--")
plt.title("Predicting Generativity or Stagnation Trends")
plt.xlabel("Time")
plt.ylabel("Contributions")
plt.legend()
plt.show()
```

---

### **5. Simulation of Generativity Initiatives Impact**  
Simulating the long-term impact of generative actions like mentorship programs or community projects.  
```python
def simulate_generativity_impact(initial_investment, return_rate, duration):
    """
    Simulate the impact of generativity actions like community investments or mentorship programs.
    """
    impacts = [initial_investment]
    for _ in range(duration):
        next_impact = impacts[-1] * (1 + return_rate)
        impacts.append(next_impact)
    return impacts

# Parameters
initial_investment = 1000  # Initial contribution
return_rate = 0.05  # Growth rate of impact
duration = 20  # Years

impacts = simulate_generativity_impact(initial_investment, return_rate, duration)

# Plot
plt.plot(impacts)
plt.title("Simulation of Generativity Initiatives Impact")
plt.xlabel("Time (Years)")
plt.ylabel("Impact Value")
plt.show()
```

---

### **6. Reinforcement Learning for Generativity Optimization**  
Training a reinforcement learning agent to choose generativity-enhancing actions.  
```python
import random

def reinforcement_learning(actions, rewards, episodes):
    """
    Use reinforcement learning to identify the best actions for maximizing generativity.
    """
    Q = {action: 0 for action in actions}
    for _ in range(episodes):
        action = random.choice(actions)
        reward = rewards[action]
        Q[action] += reward
    return Q

# Actions and associated rewards
actions = ["Mentorship", "Community Project", "Personal Growth"]
rewards = {"Mentorship": 10, "Community Project": 15, "Personal Growth": 8}

Q_values = reinforcement_learning(actions, rewards, 100)

# Print action-value estimates
print("Reinforcement Learning Action Values (Generativity Optimization):")
for action, value in Q_values.items():
    print(f"{action}: {value}")
```

---

### **7. Measuring Generativity vs. Stagnation in a Population**  
Analyzing the balance of generative vs. stagnant behaviors in a dataset.  
```python
import pandas as pd
import seaborn as sns

def measure_generativity_stagnation(data):
    """
    Analyze the distribution of generativity and stagnation scores in a population.
    """
    df = pd.DataFrame(data, columns=["Generativity", "Stagnation"])
    return df.describe()

# Sample data: Generativity and stagnation scores for individuals
data = np.random.randint(1, 10, size=(50, 2))

df_summary = measure_generativity_stagnation(data)

# Visualization
sns.boxplot(data=pd.DataFrame(data, columns=["Generativity", "Stagnation"]))
plt.title("Generativity vs. Stagnation Distribution")
plt.show()
```

---

### **Applications and Benefits:**  

1. **Growth Modeling**: Logistic functions simulate bounded but impactful generativity growth.  
2. **Decision Trees**: Classifies behaviors or strategies leading to generativity.  
3. **Network Models**: Visualize collaborative contributions in social systems.  
4. **Forecasting Trends**: Time series predict future generativity or stagnation levels.  
5. **Impact Simulation**: Long-term projections of generative initiatives' outcomes.  
6. **Reinforcement Learning**: Optimal action strategies to enhance generativity.  
7. **Population Analysis**: Data analysis identifies systemic patterns in generative behaviors.

By addressing generativity versus stagnation scientifically, these examples promote positive outcomes at individual and collective levels.
