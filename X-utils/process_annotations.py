import pandas as pd
import re
import os

# Load the CSV file
df = pd.read_csv('Annotations.csv', delimiter=',', skiprows=1)

# Replace occurrences in the code_mention attribute
df['code_mention'] = df['code_mention'].str.replace("``", '"')
df['code_mention'] = df['code_mention'].str.replace("''", '"')
df['code_mention'] = df['code_mention'].str.replace("“", '"')
df['code_mention'] = df['code_mention'].str.replace("”", '"')

# Extract the event_id and orientation from the id
df['event_id'] = df['id'].apply(lambda x: re.match(r'(\d+)_(LL|L|M|R|RR)_', x).group(1))
df['orientation'] = df['id'].apply(lambda x: re.match(r'(\d+)_(LL|L|M|R|RR)_', x).group(2))

# Create the main directory if it does not exist
main_directory = '2-matched'
os.makedirs(main_directory, exist_ok=True)

# Generate a unique directory and file name for each event_id and orientation combination
for event_id in range(10):
    for orientation in ['LL', 'L', 'M', 'R', 'RR']:
        # Filter the dataframe for the current event_id and orientation
        filtered_df = df[(df['event_id'] == str(event_id)) & (df['orientation'] == orientation)]
        
        # If the filtered dataframe is not empty, save it to a new CSV file in the appropriate directory
        if not filtered_df.empty:
            event_directory = f'{main_directory}/event_{event_id}'
            orientation_directory = f'{event_directory}/orientation_{orientation}'
            os.makedirs(orientation_directory, exist_ok=True)
            file_name = f'{orientation_directory}/{event_id}_{orientation}_annotations.csv'
            # filtered_df.drop(columns=['event_id', 'orientation'], inplace=True)
            filtered_df.to_csv(file_name, index=False)
            print(f'Created file: {file_name}')