import json

def merge_json_arrays(input_filename, output_filename):
    try:
        # Load JSON data from file
        with open(input_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Merge all arrays into a single list
        merged_array = []
        for key in data:
            if isinstance(data[key], list):
                merged_array.extend(data[key])
        
        # Save merged array to new JSON file
        with open(output_filename, 'w', encoding='utf-8') as file:
            json.dump(merged_array, file, indent=4)
        
        print(f"Merged JSON saved as {output_filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_file = input("Enter input JSON file name: ")
    output_file = input("Enter output JSON file name: ")
    merge_json_arrays(input_file, output_file)