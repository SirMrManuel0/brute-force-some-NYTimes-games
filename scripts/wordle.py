import json



numV = {
    "b": 0,
    "y": 1,
    "g": 2
}


def is_not_a_number(c):
    try:
        float(c)
        return False
    except ValueError:
        return True


def filter_words(word, words):
    
    while True:
        inputs = {
            word[0]: input(word[0].upper() + ": ").lower(),
            word[1]: input(word[1].upper() + ": ").lower(),
            word[2]: input(word[2].upper() + ": ").lower(),
            word[3]: input(word[3].upper() + ": ").lower(),
            word[4]: input(word[4].upper() + ": ").lower()
        }
        
        if all([len(i) == 1 and is_not_a_number(i) and i in (key for key, val in numV.items()) for key, i in inputs.items()]):
            break
        else:
            print("\nWrong input!\n")
    
    inputs = {key: numV[val] for key, val in inputs.items()}
    
    for index, vals in enumerate(inputs.items()):
        letter = vals[0]
        val = vals[1]
        if val == numV["g"]:
            words = [word for word in words if word[index] == letter]
        elif val == numV["y"]:
            words = [word for word in words if word[index] != letter and letter in word]
        elif val == numV["b"]:
            words = [word for word in words if not letter in word]
    
    
    return words


def index():
    
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

        Then there will be a new word until you solve the wordle or run out of tries.
                
        As your first word, use SALET.
        
              
    """)    
    
    words = {}
    
    with open("english-words/words_dictionary_wordle.json", "r", encoding="utf-8") as f:
        words = json.load(f)
        words = [word for word, value in words.items()]
    
    words = filter_words("salet", words)

    while True:
        try:
            if len(words) == 1:
                print()
                print(words[0])
                print()
                print("Hopefully this is right.")
                print("There are no further possible words in the list.")
                print()
                break
            
            print()
            print(words[0])
            print()
            words = filter_words(words[0], words)
        except:
            print("sadly there are no correct words in the word list")
            break