Here’s a series of **7 advanced code examples** that provide actionable ways to allocate **time, energy, and attention responsibly** while avoiding unnecessary drains caused by **parasitic relationships** or inefficiencies. These examples incorporate **reliable math**, **clear reasoning**, **structured science**, and **best practices**.

---

### Smart File Name:  
**`Efficient_Time_Energy_Allocation_No_Fake_Friends.py`**

---

### Code Examples

#### 1. **Assessing Energy Drains Using a Weighted Network Model**
```python
import networkx as nx
import numpy as np

# Create a graph representing relationships
G = nx.DiGraph()

# Add nodes and weighted edges (weights represent energy cost)
relationships = [
    ("You", "Friend_A", 0.8),  # Fake friend: high energy drain
    ("You", "Friend_B", 0.2),  # Supportive friend: low energy drain
    ("You", "Coworker_A", 0.5),
    ("You", "Parasitic_Person", 0.9),  # Parasitic: very high energy drain
]

G.add_weighted_edges_from(relationships)

# Calculate total energy drain
energy_drain = sum(weight for _, _, weight in G.edges(data="weight"))
print(f"Total Energy Drain: {energy_drain:.2f}")

# Identify high-drain relationships
threshold = 0.7  # Threshold for excessive energy drain
high_drain = [(u, v) for u, v, w in G.edges(data="weight") if w > threshold]
print(f"High-Drain Relationships: {high_drain}")
```

---

#### 2. **Time Allocation Optimization Using Linear Programming**
```python
from scipy.optimize import linprog

# Define relationship categories
relationships = ["Work", "Supportive Friends", "Parasitic People", "Family"]

# Define time required per relationship category (in hours/week)
time_costs = [10, 5, 15, 8]

# Define benefit values (higher for supportive and family, lower for parasitic)
benefits = [50, 80, -10, 60]

# Objective: Maximize benefits
c = [-b for b in benefits]  # Negate because linprog minimizes

# Constraints: Total time <= 40 hours
A = [time_costs]
b = [40]

# Bounds: 0 <= time <= max time available
bounds = [(0, t) for t in time_costs]

# Solve optimization problem
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
print("Optimal Time Allocation:", result.x)
```

---

#### 3. **Modeling Attention as a Resource Pool**
```python
# Simulate attention distribution
np.random.seed(42)

# Define categories and their attention weights
categories = ["Work", "Family", "Fake Friends", "Self-Care"]
attention_weights = [0.4, 0.3, 0.1, 0.2]  # Fractions of attention

# Simulate attention over 7 days
days = 7
attention_matrix = np.random.dirichlet(attention_weights, days)

# Display allocation
for i, day in enumerate(attention_matrix):
    print(f"Day {i + 1}: {dict(zip(categories, day))}")
```

---

#### 4. **Energy Recovery Simulation Using Logistic Growth**
```python
import matplotlib.pyplot as plt

def energy_recovery(energy, drain_rate, recovery_rate, steps):
    """
    Simulates energy recovery over time.
    """
    energies = [energy]
    for _ in range(steps):
        recovery = recovery_rate * (1 - energy / 100)
        energy = max(0, energy - drain_rate + recovery)
        energies.append(energy)
    return energies

# Parameters
initial_energy = 50
drain_rate = 5
recovery_rate = 10
steps = 30

# Simulate
energies = energy_recovery(initial_energy, drain_rate, recovery_rate, steps)

# Plot
plt.plot(energies, label="Energy Levels")
plt.axhline(50, color="red", linestyle="--", label="Threshold")
plt.xlabel("Time")
plt.ylabel("Energy Level")
plt.title("Energy Recovery Simulation")
plt.legend()
plt.show()
```

---

#### 5. **Removing Parasitic Relationships Using Centrality Metrics**
```python
# Use the graph from example 1
centrality = nx.betweenness_centrality(G, weight="weight")
parasitic_nodes = [node for node, score in centrality.items() if score > 0.6]

print("Nodes to Remove:", parasitic_nodes)

# Remove parasitic nodes
G.remove_nodes_from(parasitic_nodes)
print("Updated Network:", G.edges())
```

---

#### 6. **Tracking Personal Progress Using Exponential Smoothing**
```python
def exponential_smoothing(data, alpha):
    """
    Applies exponential smoothing to time-series data.
    """
    smoothed = [data[0]]
    for t in range(1, len(data)):
        smoothed_value = alpha * data[t] + (1 - alpha) * smoothed[-1]
        smoothed.append(smoothed_value)
    return smoothed

# Simulated weekly productivity
productivity = [50, 52, 47, 55, 60, 58, 62]

# Apply smoothing
alpha = 0.3
smoothed_productivity = exponential_smoothing(productivity, alpha)

# Plot results
plt.plot(productivity, label="Original")
plt.plot(smoothed_productivity, label="Smoothed", linestyle="--")
plt.title("Productivity Over Time")
plt.legend()
plt.show()
```

---

#### 7. **Evaluating Decisions Using Multi-Criteria Decision Analysis (MCDA)**
```python
from sklearn.preprocessing import MinMaxScaler

# Define decision options
options = ["Work Harder", "Invest in Self-Care", "Cut Fake Friends", "Seek New Opportunities"]
criteria = ["Energy Cost", "Time Cost", "Long-Term Benefit", "Emotional Impact"]

# Decision matrix (rows=options, cols=criteria)
decision_matrix = np.array([
    [8, 10, 7, 5],  # Work Harder
    [3, 4, 9, 8],   # Invest in Self-Care
    [1, 2, 10, 9],  # Cut Fake Friends
    [6, 6, 8, 7],   # Seek New Opportunities
])

# Normalize criteria (Min-Max Scaling)
scaler = MinMaxScaler()
normalized_matrix = scaler.fit_transform(decision_matrix)

# Assign weights to criteria
weights = np.array([0.3, 0.2, 0.4, 0.1])

# Calculate weighted scores
scores = normalized_matrix.dot(weights)
best_option = options[np.argmax(scores)]

print(f"Best Option: {best_option}")
print(f"Scores: {dict(zip(options, scores))}")
```

---

### Overview of Outputs:
1. **Energy Drains Analysis:** Identifies and flags high-drain relationships.  
2. **Optimized Time Allocation:** Efficient use of time for meaningful connections.  
3. **Attention Simulation:** Simulates realistic attention allocation patterns.  
4. **Energy Recovery:** Models and visualizes energy restoration trends.  
5. **Network Optimization:** Removes parasitic relationships using network theory.  
6. **Productivity Tracking:** Smooths performance trends for better decision-making.  
7. **MCDA for Decisions:** Finds the best strategic choice based on weighted benefits.

Would you like to customize further with industry-specific considerations?
