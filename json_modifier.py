import json

def doesnt_has_twice_the_same(key):
    for i, c in enumerate(key):
        if i == 0:
            continue
        if c == key[i-1]:
            return False
    
    
    
    return True

# Load JSON data from "import.json" file
with open('english-words\words_dictionary.json', 'r', encoding="utf-8") as import_file:
    json_data = json.load(import_file)

# Convert keys to lowercase in the loaded JSON data
json_data = {key.lower(): value for key, value in json_data.items()}

# Define the set of valid keys
valid_keys = {key for key, value in json_data.items() if len(key) > 2 and doesnt_has_twice_the_same(key)}

# Filter the keys and set their values to None
filtered_json_data = {key: 1 for key in valid_keys}

# Save the modified JSON data to a file
with open('english-words\words_dictionary_letterboxed.json', 'w') as file:
    json.dump(filtered_json_data, file, indent=4, ensure_ascii=False)



valid_keys = {}
json_data = {}

# Load JSON data from "import.json" file
with open('english-words\words_dictionary.json', 'r', encoding="utf-8") as import_file:
    json_data = json.load(import_file)

# Convert keys to lowercase in the loaded JSON data
json_data = {key.lower(): value for key, value in json_data.items()}

# Define the set of valid keys
valid_keys = {key: 1 for key, value in json_data.items() if len(key) == 5}

# Save the modified JSON data to a file
with open('english-words\words_dictionary_wordle.json', 'w') as file:
    json.dump(valid_keys, file, indent=4, ensure_ascii=False)