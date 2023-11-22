import json
import random

# Dictionary to map color codes to numbers
numV = {
    "b": 0,
    "y": 1,
    "g": 2
}

# Function to check if a character is not a number
def is_not_a_number(c):
    try:
        float(c)
        return False
    except ValueError:
        return True

def find_duplicates(lst):
    seen = set()
    duplicates = set(x for x in lst if x in seen or seen.add(x))
    return list(duplicates)


# Function to filter words based on user input
def filter_words(word, words):
    while True:
        # Prompt user for input for each letter in the word
        inputs = {
            "+"+word[0]: input(word[0].upper() + ": ").lower(),
            "-"+word[1]: input(word[1].upper() + ": ").lower(),
            "*"+word[2]: input(word[2].upper() + ": ").lower(),
            "/"+word[3]: input(word[3].upper() + ": ").lower(),
            ","+word[4]: input(word[4].upper() + ": ").lower()
        }
        
        if any([val == "w" for key, val in inputs.items()]):
            return -1
        
        # Check if the input is valid (single character, not a number, and in the valid color set)
        if all([len(i) == 1 and is_not_a_number(i) and i in (key for key, val in numV.items()) for key, i in inputs.items()]):
            break
        else:
            print("\nWrong input!\n")
    
    
    
    
    # Map user input to color codes
    inputs = {key: numV[val] for key, val in inputs.items()}
    
    
    if len({key for key, val in inputs.items()}) != len([key for key, val in inputs.items()]):
        list_inputs = [key for key, val in inputs.items()]
        list_inputs = find_duplicates(list_inputs)
        
        for i in list_inputs:
            values = [val for key, val in inputs.items() if key[1:] == i]
            keys = [key for key, val in inputs.items() if key[1:] == i]
            
            
            if numV['g'] in values:
                for index, val in enumerate(values):
                    if val != numV['g']:
                        inputs[keys[index]] = numV['y']
                    elif val == numV['g']:
                        inputs[keys[index]] = numV['g']
    
    
    # Filter words based on the user's input
    for index, vals in enumerate(inputs.items()):
        letter = vals[0][1:]
        val = vals[1]
        if val == numV["g"]:
            words = [word for word in words if word[index] == letter]
        elif val == numV["y"]:
            words = [word for word in words if word[index] != letter and letter in word]
        elif val == numV["b"]:
            words = [word for word in words if not letter in word]
        
            
                
    
    
    return words

# Function to display the Wordle game solver
def index():
    # Define color codes for console output
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    ORANGE = '\033[38;5;208m'
    PURPLE = '\033[38;5;129m'
    GRAY = '\033[38;5;240m'
    RESET = '\033[0m'  # Reset to default color
    
    # Display Wordle instructions
    print(""" 
    __        _____  ____  ____  _     _____ 
    \ \      / / _ \|  _ \|  _ \| |   | ____|
     \ \ /\ / | | | | |_) | | | | |   |  _|  
      \ V  V /| |_| |  _ <| |_| | |___| |___ 
       \_/\_/  \___/|_| \_|____/|_____|_____|
                                         
          
        Follow the outputs as your inputs and you will always win (maybe).
         
        After each word, you will see 5 letters.
        e.g.
        S:
        A:
        L:
        E:
        T:

        Write after each letter the right color (only the first character).
        green = g
        yellow = y
        black = b (when it is not yellow or green)
        e.g.
        S: g
        A: y
        L: b
        E: b
        T: b

        If the given word does not work and is not recognized as a word, enter w instead of g/y/b.
        
        Words marked as not working will be automatically deleted from the word list.
        
        You can also manually mark words as not working by adding them to the not_working_wordle.txt
        Make sure to seperate the words by line.

        Then there will be a new word until you solve the wordle or run out of tries.
                
        As your first word, use """ + GREEN + """SALET""" + RESET + """.
        
              
    """)
    
    
    with open("not_working_wordle.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        if len(lines) > 0:
            with open("english-words/words_dictionary_wordle.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                data = {key: val for key, val in data.items() if not key in lines}
            with open("english-words/words_dictionary_wordle.json", "w") as f:
                json.dump(data, file, ensure_ascii=False, indent=4)
                
    
    
    
    
    
    
    # Load words from a JSON file
    words = {}
    with open("english-words/words_dictionary_wordle.json", "r", encoding="utf-8") as f:
        words = json.load(f)
        words = [word for word, value in words.items()]
    
    # Filter words based on the initial word "SALET"
    words = filter_words("salet", words)

    while True:
        try:
            index = 0
            if len(words) > 1:
                index = random.randint(0, len(words) - 1)
            elif len(words) == 0:
                raise Exception("no words in the list!")
            if len(words) == 1:
                print()
                print(words[index])
                print()
                print("Hopefully this is right.")
                print("There are no further possible words in the list.")
                print()
                break
            
            print()
            print(words[index])
            print()
            temp = filter_words(words[index], words)
            if temp == -1:
                not_working_word = words.pop(index)
                with open("english-words/words_dictionary_wordle.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
                with open("english-words/words_dictionary_wordle.json", "w") as file:
                    data = {key: val for key, val in data.items() if not key == not_working_word}
                    json.dump(data, file, indent=4, ensure_ascii=False)
                with open("not_working_wordle.txt", "r", encoding="utf-8") as file:
                    lines = file.readlines()
                    lines.append(not_working_word)
                with open("not_working_wordle.txt", "w", encoding="utf-8") as file:
                    for index, i in enumerate(lines):
                        if len(lines) - 1 == index:
                            file.write(i)
                            break
                        file.write(i+"\n")
            else:
                words = temp
            
        except Exception as e:
            print(e)
            print("sadly there are no correct words in the word list")
            break