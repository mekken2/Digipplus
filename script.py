import pandas as pd

# Define the weights for the criteria
weights = {
    'Python': 0.2,
    'Machine Learning': 0.3,
    'NLP': 0.3,
    'Deep Learning': 0.3,
    'Other Skills': {
        'Python': 0.2,
        'Machine Learning': 0.1,
        'NLP': 0.1,
        'Deep Learning': 0.1
    },
    'Availability': 0.1,
    'Performance_PG': 0.15,
    'Performance_UG': 0.15,
    'Performance_12': 0.15,
    'Performance_10': 0.15
}

# Load the dataset
df = pd.read_excel('Applications_for_Machine_Learning_internship.xlsx')

# Preprocess the dataset
df['Other Skills'] = df['Other Skills'].fillna('')
df['Are you available for 3 months, starting immediately, for a full-time work from home internship?'] = df['Are you available for 3 months, starting immediately, for a full-time work from home internship?'].fillna('No')
df[['Performance_PG', 'Performance_UG', 'Performance_12', 'Performance_10']] = df[['Performance_PG', 'Performance_UG', 'Performance_12', 'Performance_10']].fillna(0)

# Define a function to calculate the score for other skills based on token words
def calculate_other_skills_score(skills):
    tokens = ['Python', 'Machine Learning', 'NLP', 'Deep Learning']
    score = sum(weights['Other Skills'].get(token, 0) for token in tokens if token in skills)
    return score

# Calculate the total score for each intern
df['Other Skills Score'] = df['Other Skills'].apply(calculate_other_skills_score)
df['Total Score'] = (
    df['Python'] / 3 * weights['Python'] +
    df['Machine Learning'] / 3 * weights['Machine Learning'] +
    df['NLP'] / 3 * weights['NLP'] +
    df['Deep Learning'] / 3 * weights['Deep Learning'] +
    df['Other Skills Score'] * weights['Other Skills'] +
    (df['Are you available for 3 months, starting immediately, for a full-time work from home internship?'] == 'Yes').astype(int) * weights['Availability'] +
    df['Performance_PG'] / 100 * weights['Performance_PG'] +
    df['Performance_UG'] / 100 * weights['Performance_UG'] +
    df['Performance_12'] / 100 * weights['Performance_12'] +
    df['Performance_10'] / 100 * weights['Performance_10']
)

# Sort the interns based on their total score in descending order
df = df.sort_values(by='Total Score', ascending=False)

# Select the top-scoring intern(s)
num_interns_to_hire = 1  # Specify the number of interns to hire
top_interns = df.head(num_interns_to_hire)

# Output the details of the selected intern(s)
for index, intern in top_interns.iterrows():
    print(f"Selected Intern {index + 1}:")
    print(f"Total Score: {intern['Total Score']}")
    # Print other relevant details from the dataset

# Notify the selected intern(s)
# Add code to send notification or feedback to the selected intern(s)
