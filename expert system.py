class SymptomCheckerExpertSystem:
    def __init__(self):
        self.rules = {
            'Fever': ['High body temperature', 'Headache', 'Fatigue'],
            'Cough': ['Persistent cough', 'Shortness of breath', 'Chest pain'],
            'Sore Throat': ['Pain or irritation in the throat', 'Difficulty swallowing'],
            'Headache': ['Persistent headache', 'Nausea', 'Sensitivity to light'],
            # Add more symptoms and related conditions as needed
        }

    def get_conditions(self, symptoms):
        conditions = []
        for condition, related_symptoms in self.rules.items():
            if all(symptom.strip().lower() in [s.lower().strip() for s in symptoms] for symptom in related_symptoms):
                conditions.append(condition)
        return conditions

def main():
    expert_system = SymptomCheckerExpertSystem()

    print("Welcome to the Symptom Checker Expert System!")
    print("Enter your symptoms (comma-separated):")
    user_input = input("Symptoms: ").split(',')

    conditions = expert_system.get_conditions(user_input)

    if conditions:
        print("Possible conditions based on your symptoms:")
        for condition in conditions:
            print(f"- {condition}")
    else:
        print("No specific conditions identified based on your symptoms. Consult a healthcare professional.")

if __name__ == "__main__":
    main()
