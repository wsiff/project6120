import json
import os

def split_json(input_file, output_dir, chunk_size):
    """
    Splits a large JSON file into smaller chunks.
    
    Args:
        input_file (str): Path to the input JSON file.
        output_dir (str): Directory to save the output chunks.
        chunk_size (int): Number of elements per chunk.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the JSON data
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Check if the data is a list
    if not isinstance(data, list):
        raise ValueError("JSON root must be an array to split.")
    
    # Split the data into chunks
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        chunk_file = os.path.join(output_dir, f'chunk_{i//chunk_size + 1}.json')
        with open(chunk_file, 'w') as chunk_file_obj:
            json.dump(chunk, chunk_file_obj, indent=4)
    
    print(f"JSON file split into chunks saved in: {output_dir}")

# Example usage
split_json('Data/Malicious/log4shell.json', 'output_chunks', 500)  # Splits into chunks of 500 items
