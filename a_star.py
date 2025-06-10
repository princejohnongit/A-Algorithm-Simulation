import heapq
from health_utils import heuristic, cost_function, update_diabetes_level, TARGET_DIABETES_LEVEL
from health_node import HealthNode

def a_star_search(start_node):
    open_list = []
    heapq.heappush(open_list, (heuristic(start_node), start_node))
    closed_list = set()

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node.diabetes_level <= TARGET_DIABETES_LEVEL:
            return current_node

        closed_list.add((current_node.bmi, current_node.activity_score, current_node.diabetes_level))

        for suggestion in current_node.suggestions:
            new_bmi = max(10, current_node.bmi - suggestion['bmi_change'])
            new_activity = min(100, current_node.activity_score + suggestion['activity_change'])
            new_diabetes_level = update_diabetes_level(suggestion['bmi_change'], suggestion['activity_change'], current_node.diabetes_level)

            new_node = HealthNode(
                new_bmi, current_node.age, new_activity, new_diabetes_level,
                suggestions=suggestion['next_suggestions'], parent=current_node
            )

            if (new_node.bmi, new_node.activity_score, new_node.diabetes_level) not in closed_list:
                g_cost = cost_function(current_node, new_node)
                f_cost = g_cost + heuristic(new_node)
                heapq.heappush(open_list, (f_cost, new_node))
    return None