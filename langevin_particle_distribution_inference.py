### **Smart File Name:**  
`langevin_particle_distribution_inference.py`

Here are **7 advanced code examples** for inferring parameter distributions in heterogeneous motile particle ensembles using a likelihood-based approach for second-order Langevin models. These examples demonstrate **brilliant math** and a **robust strategy**, focusing on practical and theoretical aspects such as likelihood estimation, particle trajectory analysis, and parameter uncertainty quantification.

---

### **1. Simulating Second-Order Langevin Dynamics**  
**Purpose:** Generate synthetic trajectories for heterogeneous motile particles based on second-order Langevin equations.

```python
import numpy as np

# Parameters
time = np.linspace(0, 10, 1000)  # Time array
mass = 1.0  # Mass of the particle
gamma = 0.5  # Friction coefficient
k = 2.0  # Spring constant
noise_std = 0.2  # Standard deviation of noise

# Langevin dynamics
def simulate_trajectory(mass, gamma, k, noise_std, time):
    dt = np.diff(time)[0]
    velocity = [0]
    position = [0]
    for t in time[1:]:
        acc = -(gamma / mass) * velocity[-1] - (k / mass) * position[-1] + np.random.normal(0, noise_std)
        new_velocity = velocity[-1] + acc * dt
        new_position = position[-1] + new_velocity * dt
        velocity.append(new_velocity)
        position.append(new_position)
    return np.array(position), np.array(velocity)

positions, velocities = simulate_trajectory(mass, gamma, k, noise_std, time)
print(f"Trajectory simulated with {len(positions)} steps.")
```

---

### **2. Likelihood Estimation for Parameter Inference**  
**Purpose:** Calculate the likelihood of observed trajectories given Langevin parameters.

```python
from scipy.stats import norm

# Parameters
observed_positions = positions + np.random.normal(0, 0.1, len(positions))
observed_velocities = velocities + np.random.normal(0, 0.1, len(velocities))

# Likelihood function
def likelihood(observed_pos, observed_vel, mass, gamma, k, noise_std, time):
    dt = np.diff(time)[0]
    model_acc = -(gamma / mass) * observed_vel[:-1] - (k / mass) * observed_pos[:-1]
    observed_acc = np.diff(observed_vel) / dt
    residuals = observed_acc - model_acc
    return np.sum(norm.logpdf(residuals, scale=noise_std))

log_likelihood = likelihood(observed_positions, observed_velocities, mass, gamma, k, noise_std, time)
print(f"Log-Likelihood: {log_likelihood:.2f}")
```

---

### **3. Parameter Optimization via Maximum Likelihood Estimation (MLE)**  
**Purpose:** Optimize Langevin parameters to maximize the likelihood.

```python
from scipy.optimize import minimize

# Objective function
def negative_log_likelihood(params):
    mass, gamma, k, noise_std = params
    return -likelihood(observed_positions, observed_velocities, mass, gamma, k, noise_std, time)

# Initial guess
initial_params = [1.0, 0.5, 2.0, 0.2]
bounds = [(0.1, 10), (0.1, 10), (0.1, 10), (0.01, 1)]

result = minimize(negative_log_likelihood, initial_params, bounds=bounds)
optimized_params = result.x
print(f"Optimized Parameters: Mass={optimized_params[0]:.2f}, Gamma={optimized_params[1]:.2f}, K={optimized_params[2]:.2f}, Noise={optimized_params[3]:.2f}")
```

---

### **4. Inferring Parameter Distributions via Bayesian Inference**  
**Purpose:** Use Markov Chain Monte Carlo (MCMC) to infer parameter distributions.

```python
import pymc3 as pm

# Bayesian model
with pm.Model() as model:
    mass = pm.Uniform("mass", lower=0.1, upper=10)
    gamma = pm.Uniform("gamma", lower=0.1, upper=10)
    k = pm.Uniform("k", lower=0.1, upper=10)
    noise_std = pm.HalfNormal("noise_std", sigma=1)
    
    # Observed data likelihood
    model_acc = -(gamma / mass) * observed_velocities[:-1] - (k / mass) * observed_positions[:-1]
    observed_acc = np.diff(observed_velocities) / np.diff(time)[0]
    residuals = observed_acc - model_acc
    likelihood = pm.Normal("likelihood", mu=residuals, sigma=noise_std, observed=0)
    
    trace = pm.sample(2000, tune=1000, cores=2)

pm.traceplot(trace)
```

---

### **5. Particle Heterogeneity Analysis via Clustering**  
**Purpose:** Cluster particles based on inferred parameters.

```python
from sklearn.cluster import KMeans

# Simulate heterogeneous parameters
num_particles = 50
heterogeneous_params = np.random.rand(num_particles, 4)  # Mass, Gamma, K, Noise

# K-Means clustering
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(heterogeneous_params)

print(f"Cluster Centers:\n{kmeans.cluster_centers_}")
```

---

### **6. Error Propagation in Parameter Inference**  
**Purpose:** Quantify uncertainty in inferred parameters due to measurement noise.

```python
from scipy.stats import bootstrap

# Bootstrapping
def bootstrap_likelihood(data, resamples=1000):
    results = bootstrap((data,), np.mean, n_resamples=resamples, confidence_level=0.95)
    return results.confidence_interval

param_ci = bootstrap_likelihood(observed_positions)
print(f"Confidence Interval for Position: {param_ci}")
```

---

### **7. Visualizing Parameter Influence on Dynamics**  
**Purpose:** Analyze the effect of varying parameters on Langevin trajectories.

```python
import matplotlib.pyplot as plt

# Vary parameters and simulate trajectories
gammas = [0.1, 0.5, 1.0]
for gamma in gammas:
    pos, vel = simulate_trajectory(mass, gamma, k, noise_std, time)
    plt.plot(time, pos, label=f"Gamma={gamma}")

plt.xlabel("Time")
plt.ylabel("Position")
plt.legend()
plt.title("Effect of Friction Coefficient on Trajectories")
plt.show()
```

---

### **Summary of Concepts and Strategy**  
This series of advanced examples delves into the **likelihood-based inference of parameter distributions in heterogeneous motile particle ensembles** governed by second-order Langevin dynamics. The examples cover trajectory simulation, maximum likelihood estimation, Bayesian inference, and clustering for heterogeneity analysis. Brilliant mathematical models and robust strategies quantify parameter uncertainties, explore their influence on dynamics, and integrate advanced visualization. This approach provides comprehensive insights into particle ensembles and lays the foundation for applications in biophysics, material science, and complex systems analysis.
