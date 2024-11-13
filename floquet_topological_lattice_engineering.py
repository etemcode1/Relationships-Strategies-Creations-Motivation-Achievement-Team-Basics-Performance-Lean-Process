### **Smart File Name:**  
`floquet_topological_lattice_engineering.py`

Here are **7 advanced code examples** focused on **Topological Floquet Engineering of a Three-Band Optical Lattice with Dual-Mode Resonant Driving**. These examples include brilliant mathematics and robust strategies for simulating, analyzing, and optimizing such systems.

---

### **1. Constructing a Three-Band Optical Lattice Hamiltonian**  
**Purpose:** Define the tight-binding Hamiltonian of a three-band optical lattice.

```python
import numpy as np
from scipy.linalg import block_diag

# Parameters
t = 1.0  # Hopping amplitude
delta = 0.5  # Band offset

# Construct three-band lattice Hamiltonian
H_0 = np.array([[delta, t, 0],
                [t, 0, t],
                [0, t, -delta]])

print(f"Static Hamiltonian (H_0):\n{H_0}")
```

---

### **2. Adding Dual-Mode Periodic Driving**  
**Purpose:** Incorporate resonant dual-mode periodic driving into the lattice Hamiltonian.

```python
omega1 = 2.0  # Frequency of first driving mode
omega2 = 3.0  # Frequency of second driving mode
A1 = 0.5      # Amplitude of first mode
A2 = 0.3      # Amplitude of second mode
phi = np.pi/2 # Phase difference

# Time-dependent driving terms
def H_drive(t):
    return np.array([[A1 * np.cos(omega1 * t), 0, A2 * np.sin(omega2 * t + phi)],
                     [0, 0, 0],
                     [A2 * np.sin(omega2 * t + phi), 0, -A1 * np.cos(omega1 * t)]])

print(f"H_drive at t=0:\n{H_drive(0)}")
```

---

### **3. Computing the Floquet Hamiltonian Using Time Averaging**  
**Purpose:** Calculate the effective Hamiltonian for the periodically driven system.

```python
from scipy.integrate import quad

# Time-averaging H_eff over one period
T = 2 * np.pi / omega1  # Period of the driving field

def H_eff():
    def time_integral(t):
        return H_0 + H_drive(t)
    H_avg = np.zeros_like(H_0)
    for i in range(H_0.shape[0]):
        for j in range(H_0.shape[1]):
            H_avg[i, j] = quad(lambda t: time_integral(t)[i, j], 0, T)[0] / T
    return H_avg

H_effective = H_eff()
print(f"Effective Floquet Hamiltonian (H_eff):\n{H_effective}")
```

---

### **4. Berry Curvature of the Floquet Bands**  
**Purpose:** Compute the Berry curvature of the Floquet bands in the Brillouin zone.

```python
def berry_curvature(kx, ky, H):
    eigvals, eigvecs = np.linalg.eigh(H)
    curvature = 0
    for n in range(len(eigvals)):
        for m in range(len(eigvals)):
            if n != m:
                num = np.imag(np.dot(eigvecs[:, n].conj(), np.dot(H, eigvecs[:, m])))
                denom = (eigvals[n] - eigvals[m])**2
                curvature += np.abs(num / denom)
    return curvature

# Sample at a point in the Brillouin zone
kx, ky = 0.1, 0.1
H_k = H_0 + H_drive(0)  # Example for H_k at t=0
print(f"Berry Curvature at (kx, ky): {berry_curvature(kx, ky, H_k)}")
```

---

### **5. Band Structure Simulation Under Periodic Driving**  
**Purpose:** Calculate and visualize the Floquet band structure.

```python
import matplotlib.pyplot as plt

# Sample points in Brillouin zone
k_values = np.linspace(-np.pi, np.pi, 100)
bands = []

for k in k_values:
    H_k = H_0 + np.cos(k) * np.eye(3)  # Simple periodic contribution
    eigvals = np.linalg.eigvalsh(H_k)
    bands.append(eigvals)

bands = np.array(bands)
plt.plot(k_values, bands[:, 0], label='Band 1')
plt.plot(k_values, bands[:, 1], label='Band 2')
plt.plot(k_values, bands[:, 2], label='Band 3')
plt.title("Floquet Band Structure")
plt.xlabel("Wave Vector (k)")
plt.ylabel("Energy (E)")
plt.legend()
plt.show()
```

---

### **6. Topological Invariant: Chern Number Calculation**  
**Purpose:** Compute the Chern number for the Floquet bands.

```python
def chebyshev_approximation(H, k_points):
    chern_number = 0
    for i, k in enumerate(k_points[:-1]):
        dk = k_points[i+1] - k
        chern_number += berry_curvature(k, k, H) * dk**2
    return chern_number

k_grid = np.linspace(-np.pi, np.pi, 50)
H_k_grid = [H_0 + H_drive(t=0.5) for _ in k_grid]
chern = chebyshev_approximation(H_k_grid, k_grid)
print(f"Computed Chern Number: {chern}")
```

---

### **7. Floquet State Stability Analysis**  
**Purpose:** Analyze the stability of the Floquet states using Floquet-Lyapunov exponents.

```python
from scipy.linalg import expm

# Calculate the Floquet operator over one period
U_F = expm(-1j * H_effective * T)

# Floquet-Lyapunov exponents (imaginary part of eigenvalues of log(U_F))
eigvals = np.linalg.eigvals(U_F)
lyapunov_exponents = np.imag(np.log(eigvals))
print(f"Floquet-Lyapunov Exponents: {lyapunov_exponents}")
```

---

### **Summary of Concepts and Math**  
These examples delve into the intricate structure of Floquet-engineered topological lattices, showcasing key operations like **Hamiltonian construction**, **Berry curvature analysis**, **Floquet operator stability**, and **Chern number computation**. By combining **time-dependent perturbation theory**, **Fourier space techniques**, and **numerical diagonalization**, these models provide a robust strategy for exploring and optimizing quantum systems under dual-mode periodic driving.
