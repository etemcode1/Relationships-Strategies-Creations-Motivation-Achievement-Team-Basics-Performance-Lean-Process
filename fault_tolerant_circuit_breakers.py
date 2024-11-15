### Circuit Breakers for Fault Tolerance: Advanced Code Examples  

1. **Basic Circuit Breaker Implementation**  
   Code demonstrates a circuit breaker class with three states: *Closed*, *Open*, and *Half-Open*. The system transitions based on failure rates and timeout periods.  
   - Includes parameters for failure thresholds and retry intervals.  
   - Features dynamic adjustment of thresholds using exponential moving averages to accommodate changing loads.  

   ```python
   class CircuitBreaker:
       def __init__(self, failure_threshold, retry_time_window):
           self.failure_threshold = failure_threshold
           self.retry_time_window = retry_time_window
           self.failures = 0
           self.state = "Closed"
           self.last_failure_time = None

       def call_service(self, service):
           if self.state == "Open":
               if time.time() - self.last_failure_time > self.retry_time_window:
                   self.state = "Half-Open"
               else:
                   raise Exception("Service is in Open state.")

           try:
               result = service()
               self.reset()
               return result
           except Exception:
               self.record_failure()
               raise

       def record_failure(self):
           self.failures += 1
           self.last_failure_time = time.time()
           if self.failures >= self.failure_threshold:
               self.state = "Open"

       def reset(self):
           self.failures = 0
           self.state = "Closed"
   ```

---

2. **Distributed Circuit Breaker with Centralized Monitoring**  
   Implements a distributed circuit breaker system for microservices, where each service reports its state to a central monitor.  
   - Tracks states of all breakers using a message queue.  
   - Uses consensus-based decision-making to coordinate responses across services.

   ```python
   import asyncio

   class DistributedCircuitBreaker:
       def __init__(self, id, monitor):
           self.id = id
           self.monitor = monitor
           self.state = "Closed"

       async def send_status(self):
           while True:
               await self.monitor.report_status(self.id, self.state)
               await asyncio.sleep(1)

       def record_failure(self):
           self.state = "Open"

   class Monitor:
       def __init__(self):
           self.statuses = {}

       async def report_status(self, service_id, state):
           self.statuses[service_id] = state
           print(f"Service {service_id}: {state}")
   ```

---

3. **Probabilistic Retry in Half-Open State**  
   A robust extension where requests in the *Half-Open* state are probabilistically retried to avoid overwhelming the service.  
   - Uses Bernoulli trials to limit retry attempts.  
   - Logs all retry outcomes for analytics.

   ```python
   import random

   def half_open_retry(service, retry_probability=0.5):
       if random.random() < retry_probability:
           try:
               return service()
           except:
               raise Exception("Service failed during retry.")
       else:
           raise Exception("Retry skipped to avoid overload.")
   ```

---

4. **Asynchronous Circuit Breaker with Timeout**  
   Supports asynchronous calls with timeout for latency-sensitive applications.  
   - Integrates asyncio to handle concurrent requests gracefully.  
   - Times out requests in *Half-Open* or *Closed* states to prevent resource hogging.

   ```python
   import asyncio

   async def async_service_call(service, timeout=2):
       try:
           result = await asyncio.wait_for(service(), timeout)
           return result
       except asyncio.TimeoutError:
           raise Exception("Service timed out.")
   ```

---

5. **Hierarchical Circuit Breaker for Dependency Chains**  
   Manages cascading failures in services with hierarchical dependencies.  
   - Implements a tree-like structure where failure in one service propagates status updates upstream.  
   - Tracks dependency graphs for efficient fault resolution.

   ```python
   class DependencyGraph:
       def __init__(self):
           self.dependencies = {}

       def add_dependency(self, parent, child):
           self.dependencies.setdefault(parent, []).append(child)

       def update_status(self, service, status):
           self.dependencies.get(service, [])
           for dependent in self.dependencies[service]:
               dependent.update_status(status)
   ```

---

6. **Dynamic Circuit Breaker with Machine Learning**  
   Predicts failure likelihood using real-time telemetry and adapts thresholds dynamically.  
   - Utilizes a logistic regression model to estimate service reliability based on metrics.  
   - Continuously trains on new data to improve performance.

   ```python
   from sklearn.linear_model import LogisticRegression
   import numpy as np

   class MLAdaptiveCircuitBreaker:
       def __init__(self):
           self.model = LogisticRegression()
           self.metrics = []
           self.labels = []

       def update_metrics(self, data, label):
           self.metrics.append(data)
           self.labels.append(label)
           self.model.fit(self.metrics, self.labels)

       def predict_failure(self, new_data):
           return self.model.predict_proba([new_data])[0][1]
   ```

---

7. **Circuit Breaker with Weighted Failures**  
   Assigns different weights to failures based on severity (e.g., latency vs. complete crash).  
   - Utilizes weighted averages to compute failure rates.  
   - Adjusts failure thresholds based on weighted counts.

   ```python
   class WeightedCircuitBreaker:
       def __init__(self, weights):
           self.weights = weights
           self.failure_score = 0
           self.state = "Closed"

       def record_failure(self, failure_type):
           self.failure_score += self.weights[failure_type]
           if self.failure_score > self.threshold:
               self.state = "Open"
   ```

--- 

### File Name Suggestion  
`fault_tolerant_circuit_breakers.py`  
