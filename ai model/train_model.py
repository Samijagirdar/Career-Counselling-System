import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Read the CSV file
data = pd.read_csv('aptitude_career_data.csv')

# Split the data into features and target
X = data[['logical_reasoning', 'numerical_ability', 'verbal_ability']]
y = data['career_path']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model to a file
with open('career_model.pkl', 'wb') as file:
    pickle.dump(model, file)
