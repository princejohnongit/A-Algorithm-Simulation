class HealthNode:
    def __init__(self, bmi, age, activity_score, diabetes_level, suggestions=None, parent=None):
        self.bmi = bmi
        self.age = age
        self.activity_score = activity_score
        self.diabetes_level = diabetes_level
        self.suggestions = suggestions or []
        self.parent = parent

    def __lt__(self, other):
        return self.diabetes_level < other.diabetes_level

    def __repr__(self):
        return f"(BMI: {self.bmi}, Activity: {self.activity_score}, Diabetes Level: {self.diabetes_level})"