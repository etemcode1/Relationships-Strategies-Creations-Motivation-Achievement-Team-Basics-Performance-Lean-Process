Here are 7 advanced code examples designed to model and analyze the anomalous diffusion of active Brownian particles in responsive elastic gels, focusing on nonergodicity, non-Gaussianity, and distributions of trapping times. These examples capture key aspects of particle behavior within complex materials, including the irregular dynamics of particle diffusion, distributions of trapping times, and statistical measures of non-Gaussianity. Each example is crafted to help researchers and teams better understand particle movement in viscoelastic environments, providing robust insights into material science and biophysics.

### Smart File Name
`AnomalousDiffusion_ABP_ElasticGels.py`

---

### Code Examples

1. **Simulating Anomalous Diffusion in Elastic Gels**  
   This example initializes an anomalous diffusion model for active Brownian particles within an elastic gel, simulating random movements with varying persistence times to mimic the irregular particle behavior typical in such systems.

   ```python
   import numpy as np
   import matplotlib.pyplot as plt

   def anomalous_diffusion(steps, alpha=0.5):
       positions = np.zeros(steps)
       for i in range(1, steps):
           step = np.random.normal(0, 1) * (i**alpha)
           positions[i] = positions[i - 1] + step
       return positions

   steps = 1000
   positions = anomalous_diffusion(steps)
   plt.plot(range(steps), positions)
   plt.xlabel("Time")
   plt.ylabel("Position")
   plt.title("Anomalous Diffusion in Elastic Gel")
   plt.show()
   ```

2. **Nonergodicity Analysis Using Time-Averaged vs. Ensemble-Averaged MSD**  
   This code compares time-averaged and ensemble-averaged mean square displacement (MSD) to explore nonergodic properties, where individual particle behaviors diverge from ensemble statistics.

   ```python
   def mean_square_displacement(positions):
       return np.mean(positions**2)

   time_averaged_MSD = [mean_square_displacement(positions[:i]) for i in range(1, len(positions))]
   ensemble_MSD = mean_square_displacement(positions)

   print(f"Time-averaged MSD: {time_averaged_MSD[-1]}")
   print(f"Ensemble-averaged MSD: {ensemble_MSD}")
   ```

3. **Non-Gaussianity Factor Calculation for Trapping Analysis**  
   Calculates the non-Gaussianity factor (NGF) to determine deviations from Gaussian behavior, identifying trapping and subdiffusive dynamics in particle movement.

   ```python
   def non_gaussianity_factor(positions):
       mean_sq_displacement = np.mean(positions**2)
       fourth_moment = np.mean(positions**4)
       ngf = (fourth_moment / (3 * mean_sq_displacement**2)) - 1
       return ngf

   ngf = non_gaussianity_factor(positions)
   print(f"Non-Gaussianity Factor: {ngf}")
   ```

4. **Generating Trapping Time Distributions**  
   This example simulates trapping events by generating distributions of trapping times for particles within elastic gels, mimicking the irregular capture and release processes within the material.

   ```python
   def trapping_times(num_traps, mean_time, std_dev):
       return np.abs(np.random.normal(mean_time, std_dev, num_traps))

   trapping_distribution = trapping_times(100, 5, 2)
   plt.hist(trapping_distribution, bins=20)
   plt.xlabel("Trapping Time")
   plt.ylabel("Frequency")
   plt.title("Distribution of Trapping Times")
   plt.show()
   ```

5. **Analyzing Long-Tail Distributions of Particle Step Lengths**  
   Models and visualizes the long-tail distribution of particle step lengths, a common feature in anomalous diffusion, to identify rare, large steps typical of active Brownian particles.

   ```python
   def step_length_distribution(steps, scale=1.0):
       return np.random.pareto(1.5, steps) * scale

   steps = 1000
   lengths = step_length_distribution(steps)
   plt.hist(lengths, bins=30, density=True)
   plt.xlabel("Step Length")
   plt.ylabel("Probability Density")
   plt.title("Long-Tail Distribution of Step Lengths")
   plt.show()
   ```

6. **Computing Fractional Brownian Motion (fBM) Trajectories**  
   This example generates fractional Brownian motion trajectories, which represent the memory effects and correlations observed in non-Markovian systems such as viscoelastic gels.

   ```python
   from fbm import FBM

   def fractional_brownian_motion(H, steps):
       fbm = FBM(n=steps, hurst=H)
       return fbm.fbm()

   H = 0.3  # Hurst parameter for subdiffusive behavior
   steps = 1000
   fbm_trajectory = fractional_brownian_motion(H, steps)
   plt.plot(fbm_trajectory)
   plt.xlabel("Time")
   plt.ylabel("Position")
   plt.title("Fractional Brownian Motion (fBM) Trajectory")
   plt.show()
   ```

7. **Power Law Fitting for Trapping Time and Step Length Distributions**  
   Fits power law distributions to trapping times and step lengths to identify scaling properties, typical in systems exhibiting anomalous diffusion and long-tail behavior.

   ```python
   from scipy.stats import powerlaw

   def fit_power_law(data):
       shape, loc, scale = powerlaw.fit(data)
       return shape, loc, scale

   shape, loc, scale = fit_power_law(trapping_distribution)
   print(f"Power Law Parameters - Shape: {shape}, Location: {loc}, Scale: {scale}")
   ```

---

### Summary and Benefits
These code examples provide a comprehensive toolkit for investigating the anomalous diffusion of active Brownian particles in elastic gels, exploring key properties like nonergodicity, non-Gaussianity, and trapping times. By modeling particle trajectories, calculating deviations from Gaussian behavior, and examining memory effects, researchers and engineers can gain insights into complex material behaviors. This toolkit benefits teams working in biophysics, materials science, and particle physics by delivering a structured, in-depth approach to analyzing particle behavior in viscoelastic and non-Newtonian materials.
