import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. LOAD AND ANALYZE THE DATA
CSV_FILE = "football_matches.csv"

if not os.path.exists(CSV_FILE):
    print(f"Error: '{CSV_FILE}' not found. Please create the file first!")
    exit()

df = pd.read_csv(CSV_FILE)

print("==================================================")
# Data Analysis Step: Let's see some basic insights
print("--- HISTORICAL DATA ANALYSIS ---")
print(f"Total historical matches analyzed: {len(df)}")
print("\nAverage stats per match outcome:")
print(df.groupby('Match_Outcome')[['Attack_Score', 'Defense_Score']].mean())

print("\nHome vs Away Win Distribution:")
print(pd.crosstab(df['Home_Advantage'], df['Match_Outcome']))
print("==================================================\n")


# 2. PREPARE THE DATA FOR AI TRAINING
# 'X' represents the features/inputs the AI will look at
X = df[['Attack_Score', 'Defense_Score', 'Home_Advantage']]

# 'y' represents the target/output the AI wants to predict
y = df['Match_Outcome']


# 3. TRAIN THE AI MODEL
# Initialize our Decision Tree AI Model
ai_model = DecisionTreeClassifier(random_state=42)

# Train (fit) the model using our historical data
ai_model.fit(X, y)

print("AI Training Status: Successfully Trained on Historical Data!\n")


# 4. INTERACTIVE USER INTERFACE FOR PREDICTIONS
def get_user_prediction():
    print("====== AI FOOTBALL MATCH RESULT PREDICTOR ======")
    try:
        attack = int(input("Enter Team's Attack Score (50-99): "))
        defense = int(input("Enter Team's Defense Score (50-99): "))
        home = int(input("Is the team playing at Home? (1 for Yes, 0 for No): "))
        
        # Structure the user input into a small DataFrame so the AI can read it
        user_data = pd.DataFrame([[attack, defense, home]], 
                                 columns=['Attack_Score', 'Defense_Score', 'Home_Advantage'])
        
        # Let the AI make a prediction
        prediction = ai_model.predict(user_data)[0]
        
        # Calculate probability/confidence of the prediction
        probabilities = ai_model.predict_proba(user_data)[0]
        max_confidence = max(probabilities) * 100
        
        print("\n-------------------------------------------")
        print(f"🤖 AI Prediction: The team will likely **{prediction.upper()}**")
        print(f"🎯 Confidence Level: {max_confidence:.1f}%")
        print("-------------------------------------------")
        
    except ValueError:
        print("\n❌ Invalid Input! Please enter numbers only.")

# Run the prediction interface
while True:
    get_user_prediction()
    choice = input("\nDo you want to predict another match? (yes/no): ").lower().strip()
    if choice != 'yes':
        print("\nThank you for using AI Football Predictor!")
        break
    print("\n" + "="*50 + "\n")