import pandas as pd
import os

def check_annotations(input_dir, annotations_prefix):
    
    # Iterate through the event_id and orientations
    for event_id in range(9):    #range(10)
        event_dir = os.path.join(input_dir, f'event_{event_id}')
        if not os.path.exists(event_dir):
            continue
        
        for orientation in ['LL', 'L', 'M', 'R', 'RR']:   # ['LL', 'L', 'M', 'R', 'RR']

            orientation_dir = os.path.join(event_dir, f'orientation_{orientation}')
            if not os.path.exists(orientation_dir):
                continue


            annotations_file = f'{event_id}_{orientation}_{annotations_prefix}'
            annotations_path = os.path.join(orientation_dir, annotations_file)

            # Load the CSV file
            df = pd.read_csv(annotations_path, delimiter=',')
            
            # Sort the DataFrame by sentence, start, and end
            df = df.sort_values(by=['sentence', 'start', 'end'])

            for filename in os.listdir(orientation_dir):
                if filename.endswith('_sent.txt'):
                    file_path = os.path.join(orientation_dir, filename)
                    
                    with open(file_path, 'r', encoding='utf-8') as file:
                        sentences = file.readlines()
                    

                    for _, row in df.iterrows():
                        code_mention = row['code_mention']
                        sentence_idx = row['sentence']
                        check_sentence = sentences[sentence_idx]

                        if code_mention not in check_sentence:
                            print(f'Sentence idx "{sentence_idx}" = {check_sentence}, \n does not contain "{code_mention}"')
                            return sentence_idx

                    
    return None  # Return None if all code mentions are found in their respective sentences

# Specify the directory containing the unprocessed files and the annotations CSV file
input_directory = 'unprocessed'
annotations_prefix = 'annotations.csv'
result = check_annotations(input_directory, annotations_prefix)

if result is not None:
    print(f'Code mention not found in sentence at index: {result}')
else:
    print('All code mentions are found in their respective sentences.')
