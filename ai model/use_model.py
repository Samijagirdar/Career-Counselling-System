import pickle

# Load the trained model
with open('career_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Example scores from a user (replace with actual data)
user_scores = [[9,1,2]]  # Example: [logical_reasoning, numerical_ability, verbal_ability]

# Predict the engineering career path
predicted_career = model.predict(user_scores)

print(f"Predicted Engineering Career Path: {predicted_career[0]}")
