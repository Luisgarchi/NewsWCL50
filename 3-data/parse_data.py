import os
import json
import csv

def process_directory(base_dir):
    data = []

    for event_id in range(10):
        event_dir = os.path.join(base_dir, f'event_{event_id}')
        for orientation_id in ["LL", "L", "M", "R", "RR"]:
            orientation_dir = os.path.join(event_dir, f'orientation_{orientation_id}')
            
            # Construct file paths
            sent_file = os.path.join(orientation_dir, f'{event_id}_{orientation_id}_sent.txt')
            annotations_file = os.path.join(orientation_dir, f'{event_id}_{orientation_id}_annotations.csv')
            
            # Read sentences
            sentences = []
            with open(sent_file, 'r') as sf:
                sentences = sf.readlines()
            
            # Read annotations
            annotations = []
            with open(annotations_file, 'r') as af:
                csv_reader = csv.DictReader(af)
                for row in csv_reader:
                    annotations.append(row)
            
            # Organize data
            for i, sentence in enumerate(sentences):
                sentence_data = {
                    "id": f"{event_id}_{orientation_id}_{i}",
                    "sentence": sentence.strip(),
                    "annotations": []
                }
                
                for annotation in annotations:
                    if int(annotation["sentence"]) == i:
                        annotation_data = {
                            "code_type": annotation["code_type"],
                            "code_name": annotation["code_name"],
                            "code_mention": annotation["code_mention"],
                            "target_concept": annotation["target_concept"],
                            #"start": annotation["start"],
                            #"end": annotation["end"]
                        }
                        sentence_data["annotations"].append(annotation_data)
                
                data.append(sentence_data)
    
    return data

def process_directory_single_annotation(base_dir):
    data = []

    for event_id in range(10):
        event_dir = os.path.join(base_dir, f'event_{event_id}')
        for orientation_id in ["LL", "L", "M", "R", "RR"]:
            orientation_dir = os.path.join(event_dir, f'orientation_{orientation_id}')
            
            # Construct file paths
            sent_file = os.path.join(orientation_dir, f'{event_id}_{orientation_id}_sent.txt')
            annotations_file = os.path.join(orientation_dir, f'{event_id}_{orientation_id}_annotations.csv')
            
            # Read sentences
            sentences = []
            with open(sent_file, 'r') as sf:
                sentences = sf.readlines()
            
            # Read annotations
            annotations = []
            with open(annotations_file, 'r') as af:
                csv_reader = csv.DictReader(af)
                for row in csv_reader:
                    annotations.append(row)
            
            # Organize data
            for i, sentence in enumerate(sentences):
                annotation_index = 0
                for annotation in annotations:
                    if int(annotation["sentence"]) == i:
                        sentence_data = {
                            "id": f"{event_id}_{orientation_id}_{i}_{annotation_index}",
                            "sentence": sentence.strip(),
                            "code_type": annotation["code_type"],
                            "code_name": annotation["code_name"],
                            "code_mention": annotation["code_mention"],
                            "target_concept": annotation["target_concept"],
                            #"start": annotation["start"],
                            #"end": annotation["end"]
                        }
                        data.append(sentence_data)
                        annotation_index += 1
    
    return data

def save_to_json(data, output_file):
    with open(output_file, 'w') as of:
        json.dump(data, of, indent=4)

if __name__ == "__main__":
    base_directory = "../2-matched"
    
    # Process data with multiple annotations per sentence
    output_json = "collapsed_data.json"
    processed_data = process_directory(base_directory)
    save_to_json(processed_data, output_json)
    print(f"Data has been processed and saved to {output_json}")
    
    # Process data with single annotation per sentence
    output_json_single_annotation = "data.json"
    processed_data_single_annotation = process_directory_single_annotation(base_directory)
    save_to_json(processed_data_single_annotation, output_json_single_annotation)
    print(f"Data with single annotations has been processed and saved to {output_json_single_annotation}")
