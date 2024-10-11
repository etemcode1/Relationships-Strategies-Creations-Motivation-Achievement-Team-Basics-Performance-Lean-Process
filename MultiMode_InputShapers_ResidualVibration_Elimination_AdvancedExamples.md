Here are **five advanced code examples** for implementing **multi-mode input shapers** to eliminate residual vibrations in dynamic systems, with a focus on robust and efficient problem-solving using advanced programming structures.

### 1. **Frequency-Based Multi-Mode Input Shaper Design (Python/NumPy)**

This example shows how to design a multi-mode input shaper by targeting multiple vibration frequencies of a dynamic system using Python's numerical capabilities.

```python
import numpy as np
import matplotlib.pyplot as plt

def input_shaper(frequencies, damping_ratios, time_step=0.001, duration=10):
    time = np.arange(0, duration, time_step)
    shaper = np.ones_like(time)
    
    for f, z in zip(frequencies, damping_ratios):
        wn = 2 * np.pi * f  # Natural frequency (rad/s)
        wd = wn * np.sqrt(1 - z**2)  # Damped natural frequency
        impulse_response = np.exp(-z * wn * time) * np.cos(wd * time)
        shaper *= impulse_response
    
    return time, shaper

frequencies = [1.0, 2.0, 3.0]  # Hz
damping_ratios = [0.1, 0.05, 0.02]
time, shaper = input_shaper(frequencies, damping_ratios)

plt.plot(time, shaper)
plt.title('Multi-Mode Input Shaper')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
```

### 2. **Optimizing Input Shaper Parameters using Genetic Algorithm (Python/Scikit-learn)**

This code example demonstrates using a genetic algorithm (GA) to optimize the input shaper parameters for multiple vibrational modes, ensuring minimal residual vibration.

```python
import numpy as np
from scipy.optimize import differential_evolution
import matplotlib.pyplot as plt

def objective(params):
    f, z = params[:3], params[3:]  # Frequency and damping ratio
    time, shaper = input_shaper(f, z)
    return np.abs(shaper[-1])  # Minimize residual vibration at final time

bounds = [(0.5, 3.0), (0.5, 3.0), (0.5, 3.0), (0.01, 0.1), (0.01, 0.1), (0.01, 0.1)]
result = differential_evolution(objective, bounds)

opt_frequencies = result.x[:3]
opt_damping_ratios = result.x[3:]
time, opt_shaper = input_shaper(opt_frequencies, opt_damping_ratios)

plt.plot(time, opt_shaper)
plt.title('Optimized Multi-Mode Input Shaper')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
```

### 3. **Multi-Mode Input Shaper for Vibration Control in a Robotic Arm (C++)**

In this example, we create an input shaper for a robotic arm system to control multi-mode vibrations.

```cpp
#include <iostream>
#include <vector>
#include <cmath>

class InputShaper {
public:
    std::vector<double> frequencies;
    std::vector<double> damping_ratios;

    InputShaper(const std::vector<double>& freqs, const std::vector<double>& zetas) 
        : frequencies(freqs), damping_ratios(zetas) {}

    std::vector<double> generateShaper(double timeStep, double duration) {
        int steps = duration / timeStep;
        std::vector<double> shaper(steps, 1.0);

        for (size_t i = 0; i < frequencies.size(); i++) {
            double wn = 2 * M_PI * frequencies[i];
            double wd = wn * sqrt(1 - pow(damping_ratios[i], 2));

            for (int t = 0; t < steps; t++) {
                double time = t * timeStep;
                shaper[t] *= exp(-damping_ratios[i] * wn * time) * cos(wd * time);
            }
        }
        return shaper;
    }
};

int main() {
    std::vector<double> freqs = {1.0, 2.0, 3.0};  // Hz
    std::vector<double> zetas = {0.1, 0.05, 0.02};
    InputShaper shaper(freqs, zetas);

    std::vector<double> result = shaper.generateShaper(0.001, 10.0);
    for (double val : result) {
        std::cout << val << std::endl;
    }
    return 0;
}
```

### 4. **MATLAB Simulation for Multi-Mode Input Shaper (MATLAB)**

This MATLAB example shows how to simulate multi-mode input shapers and visualize the system’s response.

```matlab
frequencies = [1.0, 2.0, 3.0]; % Hz
damping_ratios = [0.1, 0.05, 0.02];
time_step = 0.001;
duration = 10;

time = 0:time_step:duration;
shaper = ones(size(time));

for i = 1:length(frequencies)
    wn = 2 * pi * frequencies(i); % Natural frequency
    wd = wn * sqrt(1 - damping_ratios(i)^2); % Damped frequency
    impulse_response = exp(-damping_ratios(i) * wn * time) .* cos(wd * time);
    shaper = shaper .* impulse_response;
end

figure;
plot(time, shaper);
title('Multi-Mode Input Shaper');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;
```

### 5. **Real-Time Input Shaper for Mechanical Systems (Java)**

This example uses a real-time input shaper for a mechanical system to eliminate residual vibrations.

```java
public class InputShaper {
    private double[] frequencies;
    private double[] dampingRatios;

    public InputShaper(double[] frequencies, double[] dampingRatios) {
        this.frequencies = frequencies;
        this.dampingRatios = dampingRatios;
    }

    public double[] generateShaper(double timeStep, double duration) {
        int steps = (int) (duration / timeStep);
        double[] shaper = new double[steps];
        for (int i = 0; i < steps; i++) {
            shaper[i] = 1.0;
        }

        for (int i = 0; i < frequencies.length; i++) {
            double wn = 2 * Math.PI * frequencies[i];
            double wd = wn * Math.sqrt(1 - Math.pow(dampingRatios[i], 2));
            for (int t = 0; t < steps; t++) {
                double time = t * timeStep;
                shaper[t] *= Math.exp(-dampingRatios[i] * wn * time) * Math.cos(wd * time);
            }
        }
        return shaper;
    }

    public static void main(String[] args) {
        double[] frequencies = {1.0, 2.0, 3.0};
        double[] dampingRatios = {0.1, 0.05, 0.02};
        InputShaper inputShaper = new InputShaper(frequencies, dampingRatios);
        double[] shaper = inputShaper.generateShaper(0.001, 10.0);

        for (double val : shaper) {
            System.out.println(val);
        }
    }
}
```

---

### Summary:
These code examples illustrate various programming structures across multiple languages to solve the problem of eliminating residual vibrations using **multi-mode input shapers**. The strongest programming approaches are used to target different aspects of the problem, such as optimization, simulation, and real-time control.
