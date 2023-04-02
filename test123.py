import json

def parse_instructions(file_path):
    data = []
    try:
        with open(file_path) as f:
            json_data = json.load(f)
            for item in json_data:
                if all(key in item for key in ['motor_l', 'motor_r', 'speed_l', 'speed_r', 'direction_l', 'direction_r']):
                    data.append(item)
                else:
                    print(f"Error: Missing key value pairs in item: {item}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return data

parse_instructions('instructions.drive')