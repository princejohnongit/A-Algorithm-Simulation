import tkinter as tk
import heapq
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Constants for sensitivity
alpha = 2.5  # Sensitivity of BMI change
beta = 0.1   # Sensitivity of Activity score change
TARGET_DIABETES_LEVEL = 50  # Target diabetes level

# Define the Node class (State equivalent)
class HealthNode:
    def __init__(self, bmi, age, activity_score, diabetes_level, suggestions=None, parent=None):
        self.bmi = bmi
        self.age = age
        self.activity_score = activity_score
        self.diabetes_level = diabetes_level  # represents the current diabetes risk level
        self.suggestions = suggestions or []  # suggestions for improvement
        self.parent = parent

    def __lt__(self, other):
        return self.diabetes_level < other.diabetes_level

    def __repr__(self):
        return f"(BMI: {self.bmi}, Activity: {self.activity_score}, Diabetes Level: {self.diabetes_level})"

# Heuristic function: estimates how far the current state is from the goal
def heuristic(node):
    # Heuristic is the absolute difference from the target diabetes level
    return abs(node.diabetes_level - TARGET_DIABETES_LEVEL)

# Cost function: Calculate cost based on BMI and Activity changes
def cost_function(current, child):
    # Cost is the total effort in changing BMI and Activity score
    bmi_change = abs(current.bmi - child.bmi)
    activity_change = abs(current.activity_score - child.activity_score)
    return bmi_change + activity_change

# Function to calculate the new diabetes level after a change in BMI and Activity
def update_diabetes_level(bmi_change, activity_change, current_diabetes_level):
    # Apply the change to the diabetes level based on the formula
    reduction = alpha * bmi_change + beta * activity_change
    new_diabetes_level = max(10, current_diabetes_level - reduction)  # Ensure diabetes level doesn't go below 10
    return new_diabetes_level

# A* search algorithm to find the best health improvement path
def a_star_search(start_node):
    open_list = []
    heapq.heappush(open_list, (heuristic(start_node), start_node))
    closed_list = set()

    while open_list:
        current_f_cost, current_node = heapq.heappop(open_list)

        if current_node.diabetes_level <= TARGET_DIABETES_LEVEL:
            return current_node  # Goal reached

        closed_list.add((current_node.bmi, current_node.activity_score, current_node.diabetes_level))

        # Generate child nodes (new health suggestions based on current state)
        for suggestion in current_node.suggestions:
            new_bmi = max(10, current_node.bmi - suggestion['bmi_change'])  # Avoid negative BMI
            new_activity = min(100, current_node.activity_score + suggestion['activity_change'])  # Cap activity score at 100
            new_diabetes_level = update_diabetes_level(suggestion['bmi_change'], suggestion['activity_change'], current_node.diabetes_level)

            new_node = HealthNode(new_bmi, current_node.age, new_activity, new_diabetes_level, suggestions=suggestion['next_suggestions'], parent=current_node)

            if (new_node.bmi, new_node.activity_score, new_node.diabetes_level) not in closed_list:
                g_cost = cost_function(current_node, new_node)
                f_cost = g_cost + heuristic(new_node)
                heapq.heappush(open_list, (f_cost, new_node))

    return None  # No valid path found

# Build the user interface (UI) using tkinter
def submit_data():
    bmi = float(bmi_entry.get())
    age = int(age_entry.get())
    activity_score = int(activity_entry.get())
    diabetes_level = float(diabetes_entry.get())  # Get user-provided diabetes level

    # Example suggestions for health improvement
    suggestions = [
        {'bmi_change': 2, 'activity_change': 5, 'next_suggestions': []},
        {'bmi_change': 0.5, 'activity_change': 6, 'next_suggestions': []},
    ]

    # Define the start node with input data
    start_node = HealthNode(bmi=bmi, age=age, activity_score=activity_score, diabetes_level=diabetes_level, suggestions=suggestions)
    
    result_node = a_star_search(start_node)

    if result_node:
        result_label.config(text="Health improvement path found!")
        display_path(result_node)
        plot_graph(result_node)
    else:
        result_label.config(text="No valid path to improve health.")

# Function to display the health improvement path
def display_path(node):
    path = []
    while node:
        path.append(f"BMI: {node.bmi}, Age: {node.age}, Activity: {node.activity_score}, Diabetes Level: {node.diabetes_level}")
        node = node.parent
    path.reverse()
    path_label.config(text="\n".join(path))

# Function to extract the path data for plotting
def extract_path_data(node):
    bmi_values = []
    activity_values = []
    diabetes_level_values = []
    while node:
        bmi_values.append(node.bmi)
        activity_values.append(node.activity_score)
        diabetes_level_values.append(node.diabetes_level)
        node = node.parent
    bmi_values.reverse()
    activity_values.reverse()
    diabetes_level_values.reverse()
    return bmi_values, activity_values, diabetes_level_values

# Function to plot the graph
def plot_graph(node):
    bmi_values, activity_values, diabetes_level_values = extract_path_data(node)

    fig, ax = plt.subplots(3, 1, figsize=(6, 6))

    ax[0].plot(bmi_values, marker='o', color='blue', label='BMI')
    ax[0].set_title('BMI Over Time')
    ax[0].set_ylabel('BMI')
    ax[0].legend()

    ax[1].plot(activity_values, marker='o', color='green', label='Activity Score')
    ax[1].set_title('Activity Score Over Time')
    ax[1].set_ylabel('Activity Score')
    ax[1].legend()

    ax[2].plot(diabetes_level_values, marker='o', color='red', label='Diabetes Level')
    ax[2].set_title('Diabetes Level Over Time')
    ax[2].set_ylabel('Diabetes Level')
    ax[2].legend()

    plt.tight_layout()

    # Embed the plot in the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, columnspan=2)

# Creating the UI
root = tk.Tk()
root.title("Diabetes Health Plan")

tk.Label(root, text="BMI:").grid(row=0, column=0)
bmi_entry = tk.Entry(root)
bmi_entry.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

tk.Label(root, text="Activity Score (0-100):").grid(row=2, column=0)
activity_entry = tk.Entry(root)
activity_entry.grid(row=2, column=1)

tk.Label(root, text="Current Diabetes Level:").grid(row=3, column=0)  # New input field for diabetes level
diabetes_entry = tk.Entry(root)
diabetes_entry.grid(row=3, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=4, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=1)

path_label = tk.Label(root, text="", justify="left")
path_label.grid(row=6, column=1)

root.mainloop()
