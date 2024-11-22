### **Geminal Synergy in Pt–Co Dual-Atom Catalysts: Advanced Code Examples**  
These examples focus on modeling, simulating, and analyzing the behavior of dual-atom catalysts, particularly Pt–Co, for efficient photocatalytic hydrogen production. The solutions use computational modeling, data analysis, and machine learning for actionable insights into catalyst performance.

---

### **Smart File Name:**  
`pt_co_dual_atom_catalysis.py`

---

### **1. Catalyst Adsorption Energy Simulation**  
This script calculates adsorption energies on Pt–Co catalyst surfaces using a simplified Lennard-Jones potential.  
```python
import numpy as np

def lennard_jones_potential(r, epsilon, sigma):
    """
    Calculate the Lennard-Jones potential for given interatomic distances.
    """
    return 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)

# Parameters for Pt–Co dual-atom system
epsilon = 0.3  # Depth of the potential well (eV)
sigma = 2.8    # Distance at which potential is minimum (angstroms)
distances = np.linspace(1.5, 5, 100)  # Interatomic distances

potentials = lennard_jones_potential(distances, epsilon, sigma)

# Plot
import matplotlib.pyplot as plt
plt.plot(distances, potentials)
plt.title("Lennard-Jones Potential for Pt–Co Dual-Atom Catalyst")
plt.xlabel("Distance (Å)")
plt.ylabel("Potential Energy (eV)")
plt.grid()
plt.show()
```

---

### **2. Data Analysis of Hydrogen Evolution Reaction (HER) Efficiency**  
Analyzing experimental data to evaluate HER efficiency for Pt–Co catalysts under different conditions.  
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example dataset: HER activity under varying conditions
data = {
    "Light Intensity (W/m^2)": [100, 200, 300, 400, 500],
    "Pt Loading (wt%)": [0.5, 1.0, 1.5, 2.0, 2.5],
    "HER Rate (µmol H2/h)": [15, 30, 45, 60, 75]
}
df = pd.DataFrame(data)

# Pairplot to analyze correlations
sns.pairplot(df, diag_kind="kde")
plt.suptitle("Correlation Analysis for HER Performance", y=1.02)
plt.show()
```

---

### **3. Catalyst Surface Optimization Using Genetic Algorithm**  
Optimizing catalyst surface properties to maximize photocatalytic activity.  
```python
import random

def fitness_function(surface_area, electron_affinity):
    """
    Define a fitness function based on desired catalyst properties.
    """
    return surface_area * electron_affinity  # Simplified metric

def genetic_algorithm(generations, population_size):
    """
    Genetic algorithm to optimize catalyst surface properties.
    """
    population = [{"surface_area": random.uniform(10, 100), "electron_affinity": random.uniform(0.1, 1.0)} for _ in range(population_size)]
    for _ in range(generations):
        # Evaluate fitness
        population.sort(key=lambda x: fitness_function(x["surface_area"], x["electron_affinity"]), reverse=True)
        # Crossover
        offspring = [{"surface_area": (p1["surface_area"] + p2["surface_area"]) / 2,
                      "electron_affinity": (p1["electron_affinity"] + p2["electron_affinity"]) / 2}
                     for p1, p2 in zip(population[::2], population[1::2])]
        population = population[:population_size // 2] + offspring
    return population[0]

best_catalyst = genetic_algorithm(generations=50, population_size=20)
print("Optimized Catalyst Properties:", best_catalyst)
```

---

### **4. Machine Learning for Activity Prediction**  
Using regression to predict HER activity based on catalyst properties.  
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Dataset: catalyst properties and HER rates
features = [[0.5, 100], [1.0, 200], [1.5, 300], [2.0, 400], [2.5, 500]]  # [Pt Loading, Light Intensity]
labels = [15, 30, 45, 60, 75]  # HER Rate

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Linear regression
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.2f}")
```

---

### **5. Density of States Visualization**  
Visualizing the electronic density of states (DOS) for Pt–Co catalysts.  
```python
import numpy as np
import matplotlib.pyplot as plt

def density_of_states(energy_levels, temperature):
    """
    Simulate the density of states for a Pt–Co catalyst system.
    """
    k_b = 8.617e-5  # Boltzmann constant in eV/K
    return np.exp(-energy_levels / (k_b * temperature))

# Parameters
energy_levels = np.linspace(0, 1, 100)  # Energy levels in eV
temperature = 300  # Room temperature in Kelvin

dos = density_of_states(energy_levels, temperature)

# Plot
plt.plot(energy_levels, dos)
plt.title("Density of States for Pt–Co Catalyst")
plt.xlabel("Energy Levels (eV)")
plt.ylabel("Density of States")
plt.grid()
plt.show()
```

---

### **6. HER Efficiency Simulation under Light Irradiation**  
Modeling HER rates under varying light conditions using the Beer-Lambert Law.  
```python
def her_efficiency(light_intensity, absorption_coefficient, catalyst_efficiency):
    """
    Simulate HER efficiency under varying light intensities.
    """
    return catalyst_efficiency * (1 - np.exp(-absorption_coefficient * light_intensity))

# Parameters
light_intensity = np.linspace(50, 500, 50)  # Light intensity range in W/m^2
absorption_coefficient = 0.01
catalyst_efficiency = 0.8

her_rates = her_efficiency(light_intensity, absorption_coefficient, catalyst_efficiency)

# Plot
plt.plot(light_intensity, her_rates)
plt.title("HER Efficiency vs. Light Intensity")
plt.xlabel("Light Intensity (W/m^2)")
plt.ylabel("HER Rate (Arbitrary Units)")
plt.grid()
plt.show()
```

---

### **7. Simulating Dual-Atom Interaction Synergy**  
Simulating the synergistic effect between Pt and Co atoms in catalysis.  
```python
def dual_atom_synergy(pt_activity, co_activity, synergy_factor):
    """
    Model the synergistic effect of dual-atom interactions.
    """
    return pt_activity + co_activity + synergy_factor * pt_activity * co_activity

# Parameters
pt_activity = 0.7
co_activity = 0.5
synergy_factor = 0.3

total_activity = dual_atom_synergy(pt_activity, co_activity, synergy_factor)
print(f"Total Catalytic Activity: {total_activity}")
```

---

### **Applications and Benefits:**  
1. **Accurate Modeling**: Lennard-Jones potential aids in understanding adsorption behavior.  
2. **Data Insights**: Data analysis highlights trends in HER performance.  
3. **Optimization**: Genetic algorithms refine catalyst properties.  
4. **Prediction**: Machine learning models predict performance metrics.  
5. **Electronic Properties**: Density of states plots reveal critical insights.  
6. **Light Optimization**: Simulates HER under variable light conditions.  
7. **Synergy Modeling**: Captures the enhanced effect of dual-atom catalysts.

These examples highlight **scientific rigor** and **practical applications** for Pt–Co catalysts in **hydrogen production**.
