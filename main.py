import tkinter as tk
from a_star import a_star_search
from health_node import HealthNode
from visualization import display_path, plot_graph

def submit_data():
    bmi = float(bmi_entry.get())
    age = int(age_entry.get())
    activity_score = int(activity_entry.get())
    diabetes_level = float(diabetes_entry.get())
    suggestions = [
        {'bmi_change': 2, 'activity_change': 5, 'next_suggestions': []},
        {'bmi_change': 0.5, 'activity_change': 6, 'next_suggestions': []},
    ]
    start_node = HealthNode(bmi, age, activity_score, diabetes_level, suggestions)
    result_node = a_star_search(start_node)
    if result_node:
        result_label.config(text="Health improvement path found!")
        display_path(result_node, path_label)
        plot_graph(result_node, root)
    else:
        result_label.config(text="No valid path to improve health.")

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

tk.Label(root, text="Current Diabetes Level:").grid(row=3, column=0)
diabetes_entry = tk.Entry(root)
diabetes_entry.grid(row=3, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=4, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=1)

path_label = tk.Label(root, text="", justify="left")
path_label.grid(row=6, column=1)

root.mainloop()