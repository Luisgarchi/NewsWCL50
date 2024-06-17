import pandas as pd

def edit_annotations_file(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)
    
    # Subtract one from every sentence attribute that is greater than 16
    df.loc[df['sentence'] >= 10, 'sentence'] += 1
    
    # Save the modified DataFrame back to the CSV file
    df.to_csv(file_path, index=False)

# Specify the path to the CSV file
annotations_file_path = '9_R_annotations.csv'
edit_annotations_file(annotations_file_path)

print(f'Edited file: {annotations_file_path}')