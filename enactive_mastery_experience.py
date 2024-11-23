### **Smart File Name:**  
`enactive_mastery_experience.py`

---

### **Description:**  
Enactive Mastery Experience (EME) is a key component of Albert Bandura’s social cognitive theory, emphasizing the importance of hands-on experiences in skill development and self-efficacy. By engaging in activities that provide mastery experiences—tasks that are initially challenging but become achievable with effort—individuals build confidence in their abilities. The code examples here demonstrate how to create structured systems that simulate EME in various contexts, from learning and skill acquisition to real-time performance tracking and feedback loops. These applications provide individuals with opportunities to incrementally build mastery, ultimately leading to enhanced motivation, resilience, and overall success.

---

### **Code Examples:**

#### **1. Simulating Incremental Skill Progression through Feedback**
```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_mastery_experience(task_difficulty, learning_rate, iterations):
    """
    Simulate an enactive mastery experience where an individual progressively improves at a task.
    """
    skill_level = 0  # Initial skill level
    skill_progression = []
    
    for i in range(iterations):
        improvement = np.random.normal(learning_rate, 0.02)  # Random improvement with learning rate
        skill_level = max(0, min(100, skill_level + improvement))  # Ensure skill level stays between 0 and 100
        skill_progression.append(skill_level)
        
        # Task difficulty influences progress: harder tasks reduce progress
        skill_level -= task_difficulty * 0.1
    
    return skill_progression

# Parameters
task_difficulty = 5  # Level of task difficulty (higher means harder)
learning_rate = 1.5  # How quickly the individual improves
iterations = 50  # Number of steps in the simulation

skill_progression = simulate_mastery_experience(task_difficulty, learning_rate, iterations)

# Plot the skill progression over time
plt.plot(skill_progression)
plt.title("Skill Progression Over Time in Mastery Experience")
plt.xlabel("Iterations")
plt.ylabel("Skill Level")
plt.show()
```

---

#### **2. Mastery Feedback System with Real-Time Evaluation**
```python
def provide_feedback(current_skill, target_skill):
    """
    Provide feedback based on the difference between the current skill level and target skill level.
    Positive feedback for progress, corrective feedback for areas needing improvement.
    """
    if current_skill >= target_skill:
        return f"Great job! You have reached your target skill level of {target_skill}."
    else:
        progress = target_skill - current_skill
        return f"Keep going! You need {progress} more points to reach your target skill level."

# Example: Real-time feedback for a learner
current_skill = 45
target_skill = 60
feedback = provide_feedback(current_skill, target_skill)
print(feedback)
```

---

#### **3. Learning Task Challenge System with Gradual Difficulty Adjustment**
```python
def task_challenge_system(initial_difficulty, improvement_rate, current_skill, max_iterations):
    """
    Adjust task difficulty based on the individual's progress in order to create optimal challenges.
    As skills improve, the difficulty increases to maintain an appropriate level of challenge.
    """
    difficulties = []
    for i in range(max_iterations):
        difficulty = initial_difficulty + improvement_rate * (current_skill / 100)
        difficulties.append(difficulty)
        current_skill += np.random.normal(2, 0.5)  # Simulate skill improvement
        
    return difficulties

# Parameters
initial_difficulty = 10  # Starting difficulty of the task
improvement_rate = 0.2   # How much the task difficulty increases with skill progression
current_skill = 30       # Starting skill level
max_iterations = 50      # Number of iterations or challenges

task_difficulties = task_challenge_system(initial_difficulty, improvement_rate, current_skill, max_iterations)

# Plot the increasing difficulty over time
plt.plot(task_difficulties)
plt.title("Task Difficulty Progression in Enactive Mastery Experience")
plt.xlabel("Iterations")
plt.ylabel("Task Difficulty")
plt.show()
```

---

#### **4. Mastery Experience in Goal Setting and Achievement**
```python
def goal_setting_progress(initial_skill, target_skill, improvement_rate, max_iterations):
    """
    Simulate goal setting where an individual works towards a target skill level with gradual improvements.
    """
    current_skill = initial_skill
    achievements = []
    
    for i in range(max_iterations):
        current_skill += np.random.normal(improvement_rate, 0.5)  # Skill improvement with random variability
        achievements.append(current_skill)
        
        # Provide feedback based on progress towards target
        if current_skill >= target_skill:
            break
    
    return achievements

# Example: Goal-setting scenario where the target skill is 80
initial_skill = 50
target_skill = 80
improvement_rate = 2
max_iterations = 40

achievements = goal_setting_progress(initial_skill, target_skill, improvement_rate, max_iterations)

# Plot the achievement progress over time
plt.plot(achievements)
plt.title("Goal Setting and Achievement in Mastery Experience")
plt.xlabel("Iterations")
plt.ylabel("Skill Level")
plt.show()
```

---

#### **5. Mastery Experience Based on Personalized Learning Paths**
```python
def personalized_learning_path(start_skill, end_skill, challenge_factor, learning_sessions):
    """
    Design a personalized learning path where the difficulty is adapted to the individual's progress.
    """
    learning_progress = []
    current_skill = start_skill
    
    for session in range(learning_sessions):
        # Learning progress based on challenge factor
        current_skill += np.random.normal(learning_sessions * challenge_factor, 1)
        current_skill = min(current_skill, end_skill)  # Limit skill progression to end skill
        learning_progress.append(current_skill)
        
    return learning_progress

# Parameters
start_skill = 20
end_skill = 80
challenge_factor = 2.5
learning_sessions = 30

learning_progress = personalized_learning_path(start_skill, end_skill, challenge_factor, learning_sessions)

# Plotting the learning progression
plt.plot(learning_progress)
plt.title("Personalized Learning Path: Mastery Experience")
plt.xlabel("Learning Sessions")
plt.ylabel("Skill Level")
plt.show()
```

---

#### **6. Mastery Experience Simulator with Adaptive Feedback Loop**
```python
def adaptive_feedback_system(initial_skill, target_skill, improvement_rate, feedback_threshold, max_iterations):
    """
    Simulate an adaptive feedback system where the feedback mechanism adjusts based on the individual's performance.
    """
    skill_level = initial_skill
    feedback = []
    
    for i in range(max_iterations):
        skill_level += np.random.normal(improvement_rate, 0.5)  # Skill improvement
        if skill_level >= target_skill:
            feedback.append("Mastered! You've achieved the target skill level.")
            break
        elif skill_level > feedback_threshold:
            feedback.append("Good Progress! Keep going.")
        else:
            feedback.append("Needs Improvement. Don't give up.")
    
    return feedback

# Parameters
initial_skill = 40
target_skill = 75
improvement_rate = 2
feedback_threshold = 50
max_iterations = 50

feedback_messages = adaptive_feedback_system(initial_skill, target_skill, improvement_rate, feedback_threshold, max_iterations)
for message in feedback_messages:
    print(message)
```

---

#### **7. Real-Time Performance Tracking in Mastery Development**
```python
def track_performance_over_time(initial_skill, improvement_rate, time_steps, goal):
    """
    Track the individual's performance over time, highlighting progress toward the mastery goal.
    """
    performance = []
    current_skill = initial_skill
    
    for step in range(time_steps):
        current_skill += np.random.normal(improvement_rate, 0.5)  # Simulate skill improvement
        performance.append(current_skill)
        if current_skill >= goal:
            break
    
    return performance

# Example: Tracking performance over time towards a goal
initial_skill = 10
goal = 80
improvement_rate = 2
time_steps = 100

performance = track_performance_over_time(initial_skill, improvement_rate, time_steps, goal)

# Plot performance over time
plt.plot(performance)
plt.title("Performance Tracking in Mastery Experience")
plt.xlabel("Time Steps")
plt.ylabel("Skill Level")
plt.show()
```

---

### **Applications and Benefits:**

1. **Learning and Skill Development**: The gradual progression model promotes continuous improvement, helping individuals build confidence and mastery at their own pace.
2. **Adaptive Learning Systems**: These systems can be used in personalized learning environments where difficulty levels and feedback are adjusted based on the learner's progress, leading to higher motivation and engagement.
3. **Goal Achievement**: Goal setting and achievement are vital components of self-efficacy, and this model helps individuals see their progress over time, ensuring they remain motivated even when faced with challenges.
4. **Feedback Mechanisms**: The adaptive feedback system ensures learners receive timely and relevant guidance, making it easier to stay on track and improve.
5. **Performance Tracking**: Real-time performance tracking can be implemented to track progress toward specific goals, offering actionable insights for both learners and mentors.

By simulating enactive mastery experiences, these code examples provide a foundation for creating engaging, personalized learning environments that emphasize skill development and long-term mastery. Whether in educational, workplace, or personal growth contexts, mastery experiences foster a sense of achievement and self-efficacy.
