# A* Algorithm Simulation for Diabetes Reduction Plan

This project simulates the A* algorithm to identify a health improvement path for diabetes management. It uses a Tkinter GUI where users input their BMI, age, activity score, and diabetes level. The algorithm suggests optimal changes to reach a target diabetes level.

## Features

- **A* Pathfinding**: Find the optimal health improvement strategy using A* search.
- **User Interface**: Enter BMI, age, activity score, and diabetes level via a GUI.
- **Visualization**: Display the path and plot BMI, activity, and diabetes level changes over time.

## Usage

1. Install requirements:
    ```bash
    pip install matplotlib
    ```
2. Run the main script:
    ```bash
    python main.py
    ```
3. Enter your health data and click Submit to see suggestions and the improvement path.

## Project Structure (Modularization Recommendation)

Consider splitting the code into the following modules for better maintainability:

```
A-Algorithm-Simulation/
│
├── main.py                # Launches the GUI and handles user interaction
├── a_star.py              # Contains A* algorithm and related data structures
├── health_node.py         # Defines the HealthNode class and related logic
├── health_utils.py        # Utility functions (heuristics, cost, diabetes updates)
├── visualization.py       # Plotting and path display functions
├── README.md
```

## Example Modules

### `health_node.py`
```python
class HealthNode:
    # Node definition here

# Any HealthNode utilities
```

### `a_star.py`
```python
from health_utils import heuristic, cost_function, update_diabetes_level
from health_node import HealthNode

def a_star_search(start_node):
    # Implementation here
```

### `health_utils.py`
```python
def heuristic(node):
    # Heuristic logic

def cost_function(current, child):
    # Cost logic

def update_diabetes_level(bmi_change, activity_change, current_diabetes_level):
    # Diabetes update logic
```

### `visualization.py`
```python
def display_path(node, path_label):
    # Display logic

def plot_graph(node, root):
    # Plotting logic
```

### `main.py`
- Handles Tkinter UI, imports from above modules, and connects everything.

## Contribution

Feel free to open issues or pull requests for improvements.

## License

[Specify your license here]
