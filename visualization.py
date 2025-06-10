import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

def display_path(node, path_label):
    path = []
    while node:
        path.append(f"BMI: {node.bmi}, Age: {node.age}, Activity: {node.activity_score}, Diabetes Level: {node.diabetes_level}")
        node = node.parent
    path.reverse()
    path_label.config(text="\n".join(path))

def plot_graph(node, root):
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
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, columnspan=2)