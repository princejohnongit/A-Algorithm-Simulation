# Constants for sensitivity
ALPHA = 2.5  # Sensitivity of BMI change
BETA = 0.1   # Sensitivity of Activity score change
TARGET_DIABETES_LEVEL = 50  # Target diabetes level

def heuristic(node):
    # Heuristic is the absolute difference from the target diabetes level
    return abs(node.diabetes_level - TARGET_DIABETES_LEVEL)

def cost_function(current, child):
    # Cost is the total effort in changing BMI and Activity score
    bmi_change = abs(current.bmi - child.bmi)
    activity_change = abs(current.activity_score - child.activity_score)
    return bmi_change + activity_change

def update_diabetes_level(bmi_change, activity_change, current_diabetes_level):
    reduction = ALPHA * bmi_change + BETA * activity_change
    new_diabetes_level = max(10, current_diabetes_level - reduction)
    return new_diabetes_level