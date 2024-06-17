import spacy
import os

def preprocess_text(text):
    text = text.replace('“', '"')
    text = text.replace('”', '"')
    text = text.replace('’', "'")
    text = text.replace('‘', "'")
    return text


def process_text_files(input_dir, output_dir):

    nlp = spacy.load('en_core_web_trf')
    
    for filename in os.listdir(input_dir):

        file_path = os.path.join(input_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

            # Preprocess the text
            text = preprocess_text(text)
            
            # Process the text with spaCy
            doc = nlp(text)

            # Extract event_id and orientation from filename
            base_filename = filename.replace('.txt', '')
            event_id, orientation = base_filename.split('_')

            # Create output directory structure
            event_dir = os.path.join(output_dir, f'event_{event_id}')
            orientation_dir = os.path.join(event_dir, f'orientation_{orientation}')
            os.makedirs(orientation_dir, exist_ok=True)
            
            new_filename = base_filename + '_sent.txt'
            new_file_path = os.path.join(orientation_dir, new_filename)
            
            with open(new_file_path, 'w', encoding='utf-8') as new_file:
                for sent in doc.sents:
                    sentence = sent.text.strip()
                    if sentence:
                        new_file.write(sentence + '\n')
            
            print(f'Created file: {new_file_path}')

# Specify the directory containing the articles and the output directory
input_directory = 'process_article'
output_directory = '2-matched'
process_text_files(input_directory, output_directory)