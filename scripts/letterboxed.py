import json
import threading
import timeit
import time
import itertools

# Function to check if a character is a single character string
def is_char(c):
    if isinstance(c, str) and len(c) == 1:
        try:
            float(c)
        except ValueError:
            return True
    return False

# Function to check if two characters are not in the same row of the letters
def has_not_two_char_same_row(word, letters):
    for row in letters:
        for index, c in enumerate(word):
            if index == 0:
                continue
            if c in row and word[index-1] in row:
                return False
    return True

# Functions to find solutions with different word lengths
def two_word_solution(words, letters):
    # Counter to limit the number of printed solutions
    counter = 0
    
    # Iterate over combinations of two words from the provided list
    for a, b in itertools.combinations(words, 2):
        # Check conditions for a valid solution
        if a[-1] == b[0] and len(a) + len(b) >= 12 and {letter for letter in a} | {letter for letter in b} == letters:
            # Limit the number of printed solutions to 25
            if counter == 25:                                                                                                                 ####################
                break
            
            # Color codes for console output
            GREEN = '\033[92m'
            RESET = '\033[0m'  # Reset to default color
            
            # Print the possible combination
            print(f"{GREEN}> two word solutions > possible combination > {(a,b)}{RESET}")
            
            # Increment the counter
            counter += 1
    
def three_word_solution(words, letters):
    # Counter to limit the number of printed solutions
    counter = 0
    
    # Iterate over combinations of three words from the provided list
    for a, b, c in itertools.combinations(words, 3):
        # Check conditions for a valid solution
        if a[-1] == b[0] and b[-1] == c[0] and len(a) + len(b) + len(c) >= 12 \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} == letters:
            # Limit the number of printed solutions to 25
            if counter == 25:                                                                                                                 ####################
                break
            
            # Color codes for console output
            YELLOW = '\033[93m'
            RESET = '\033[0m'  # Reset to default color
            
            # Print the possible combination
            print(f"{YELLOW}> three word solutions > possible combination > {(a,b,c)}{RESET}")
            
            # Increment the counter
            counter += 1
    
def four_word_solution(words, letters):
    # Counter to limit the number of printed solutions
    counter = 0
    
    # Iterate over combinations of ten words from the provided list
    for a, b, c, d in itertools.combinations(words, 4):
        # Check conditions for a valid solution
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and len(a) + len(b) + len(c) + len(d) >= 12 \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | {letter for letter in d} == letters:
            # Limit the number of printed solutions to 25
            if counter == 25:                                                                                                                 ####################
                break
            
            # Color codes for console output
            BLUE = '\033[94m'
            RESET = '\033[0m'  # Reset to default color
            
            # Print the possible combination
            print(f"{BLUE}> four word solutions > possible combination > {(a,b,c,d)}{RESET}")
            
            # Increment the counter
            counter += 1
            
def five_word_solution(words, letters):
    # Counter to limit the number of printed solutions
    counter = 0
    
    # Iterate over combinations of ten words from the provided list
    for a, b, c, d, e in itertools.combinations(words, 5):
        # Check conditions for a valid solution
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and len(a) + len(b) + len(c) + len(d) + len(e) >= 12 \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | \
            {letter for letter in d} | {letter for letter in e} == letters:
            # Limit the number of printed solutions to 25
            if counter == 25:                                                                                                                 ####################
                break
            
            # Color codes for console output
            MAGENTA = '\033[95m'
            RESET = '\033[0m'  # Reset to default color
            
            # Print the possible combination
            print(f"{MAGENTA}> five word solutions > possible combination > {(a,b,c,d,e)}{RESET}")
            
            # Increment the counter
            counter += 1
            
def six_word_solution(words, letters):
    # Counter to limit the number of printed solutions
    counter = 0
    
    # Iterate over combinations of ten words from the provided list
    for a, b, c, d, e, f in itertools.combinations(words, 6):
        # Check conditions for a valid solution
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and len(a) + len(b) + len(c) + len(d) + len(e) + len(f) >= 12 \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | \
            {letter for letter in d} | {letter for letter in e} | {letter for letter in f} == letters:
            # Limit the number of printed solutions to 25
            if counter == 25:                                                                                                                 ####################
                break
            
            # Color codes for console output
            CYAN = '\033[96m'
            RESET = '\033[0m'  # Reset to default color
            
            # Print the possible combination
            print(f"{CYAN}> six word solutions > possible combination > {(a,b,c,d,e,f)}{RESET}")
            
            # Increment the counter
            counter += 1
            
def seven_word_solution(words, letters):
    # Counter to limit the number of printed solutions
    counter = 0
    
    # Iterate over combinations of ten words from the provided list
    for a, b, c, d, e, f, g in itertools.combinations(words, 7):
        # Check conditions for a valid solution
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and g[-1] == g[0] \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | \
            {letter for letter in d} | {letter for letter in e} | {letter for letter in f} | {letter for letter in g} == letters:
            # Limit the number of printed solutions to 25
            if counter == 25:                                                                                                                 ####################
                break
            
            # Color codes for console output
            RED = '\033[91m'
            RESET = '\033[0m'  # Reset to default color
            
            # Print the possible combination
            print(f"{RED}> seven word solutions > possible combination > {(a,b,c,d,e,f,g)}{RESET}")
            
            # Increment the counter
            counter += 1
            
def eight_word_solution(words, letters):
    # Counter to limit the number of printed solutions
    counter = 0
    
    # Iterate over combinations of ten words from the provided list
    for a, b, c, d, e, f, g, h in itertools.combinations(words, 8):
        # Check conditions for a valid solution
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and g[-1] == g[0] and h[-1] == h[0] \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | \
            {letter for letter in d} | {letter for letter in e} | {letter for letter in f} | \
            {letter for letter in g} | {letter for letter in h} == letters:
            # Limit the number of printed solutions to 25
            if counter == 25:                                                                                                                 ####################
                break
            
            # Color codes for console output
            ORANGE = '\033[38;5;208m'
            RESET = '\033[0m'  # Reset to default color
            
            # Print the possible combination
            print(f"{ORANGE}> eight word solutions > possible combination > {(a,b,c,d,e,f,g,h)}{RESET}")
            
            # Increment the counter
            counter += 1
        
def nine_word_solution(words, letters):
    # Counter to limit the number of printed solutions
    counter = 0
    
    # Iterate over combinations of ten words from the provided list
    for a, b, c, d, e, f, g, h, i in itertools.combinations(words, 9):
        # Check conditions for a valid solution
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and g[-1] == g[0] and h[-1] == h[0] and i[-1] == i[0] \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | \
            {letter for letter in d} | {letter for letter in e} | {letter for letter in f} | \
            {letter for letter in g} | {letter for letter in h} | {letter for letter in i} == letters:
            # Limit the number of printed solutions to 25
            if counter == 25:                                                                                                                 ####################
                break
            
            # Color codes for console output
            PURPLE = '\033[38;5;129m'
            RESET = '\033[0m'  # Reset to default color
            
            # Print the possible combination
            print(f"{PURPLE}> nine word solutions > possible combination > {(a,b,c,d,e,f,g,h,i)}{RESET}")
            
            # Increment the counter
            counter += 1
            
def ten_word_solution(words, letters):
    # Counter to limit the number of printed solutions
    counter = 0
    
    # Iterate over combinations of ten words from the provided list
    for a, b, c, d, e, f, g, h, i, j in itertools.combinations(words, 10):
        # Check conditions for a valid solution
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and g[-1] == g[0] and h[-1] == h[0] and i[-1] == i[0] and j[-1] == j[0] \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | \
            {letter for letter in d} | {letter for letter in e} | {letter for letter in f} | \
            {letter for letter in g} | {letter for letter in h} | {letter for letter in i} | {letter for letter in j}  == letters:
            # Limit the number of printed solutions to 25
            if counter == 25:                                                                                                                 ####################
                break
            
            # Color codes for console output
            GRAY = '\033[38;5;240m'
            RESET = '\033[0m'  # Reset to default color
            
            # Print the possible combination
            print(f"{GRAY}> ten word solutions > possible combination > {(a,b,c,d,e,f,g,h,i,j)}{RESET}")
            
            # Increment the counter
            counter += 1


# Main function
def index():
    # Color codes for console output
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
    
    
    
    
    # Display instructions
    print(
        """
     _     _____ _____ _____ _____ ____    ____   _____  _______ ____  
    | |   | ____|_   _|_   _| ____|  _ \  | __ ) / _ \ \/ / ____|  _ \ 
    | |   |  _|   | |   | | |  _| | |_) | |  _ \| | | \  /|  _| | | | |
    | |___| |___  | |   | | | |___|  _ <  | |_) | |_| /  \| |___| |_| |
    |_____|_____| |_|   |_| |_____|_| \_\ |____/ \___/_/\_\_____|____/ 

        
                                     1  2  3
                                     _______
                                4   |       |   12
                                5   |       |   11
                                6   |_______|   10
                            
                                     7  8  9
        
        There will be 1, """ + GREEN + """2""" + RESET + """, """ + YELLOW + """3""" + RESET + """, """ + BLUE + """4""" + RESET + """, """ + MAGENTA + """5""" + RESET + """, """ + CYAN + """6""" + RESET + """, """ + RED + """7""" + RESET + """, """ + ORANGE + """8""" + RESET + """, """ + PURPLE + """9""" + RESET + """, """ + GRAY + """10""" + RESET + """ word solutions.
        
        It is possible that some solutions do not work as the NYTimes game Letter Boxed does not have certain words in its list.
        
        max. 251 combinations if you want to change, it do it in the code.
        scripts/letterboxed.py
        search the lines with 20 #
        
        
        """
    )
    
    
    while True:
        # Input letters in a 2D array
        letters = (
                (input("1: ").lower(), input("2: ").lower(), input("3: ").lower()), 
                (input("4: ").lower(), input("5: ").lower(), input("6: ").lower()), 
                (input("7: ").lower(), input("8: ").lower(), input("9: ").lower()),
                (input("10: ").lower(), input("11: ").lower(), input("12: ").lower())
        )
        
        
        #letters = (
        #    ("i", "y", "a"),
        #    ("b", "k", "m"),
        #    ("h", "e", "l"),
        #    ("t", "c", "o")
        #)
        
        # Check if the input contains only characters
        if all([is_char(i) for ii in letters for i in ii]):
            break
        
        print("\nWrong input! Input only characters.\n")
    
    # Load words from a JSON file based on the input letters
    with open("english-words/words_dictionary_letterboxed.json", "r", encoding="utf-8") as f:
        words = json.load(f)
        words = [key for key, value in words.items() if any([key.find(i) > -1 for ii in letters for i in ii])]
        words = [word for word in words if all(letter in (item for sublist in letters for item in sublist) for letter in word)]
        words = [word for word in words if has_not_two_char_same_row(word, letters)]
        
        
    # Check for one-word solutions
    one_word_solution = [word for word in words if {letter for letter in word} == {item for sublist in letters for item in sublist}]

    if (len(one_word_solution) == 0):
            print("Sadly there are no possible one word solutions in the word list.\n")
    
    if (len(words) in [0,1]):
            print("Sadly there are no possible words in the word list.")
            return
        

    results = {}
    
    # Set of unique letters in the input
    letters = {oneletter for letter in letters for oneletter in letter}

    # Create threads for each solution length
    threads = [
        threading.Thread(target=two_word_solution, args=(words, letters), name="two"),
        threading.Thread(target=three_word_solution, args=(words, letters), name="three"),
        threading.Thread(target=four_word_solution, args=(words, letters), name="four"),
        threading.Thread(target=five_word_solution, args=(words, letters), name="five"),
        threading.Thread(target=six_word_solution, args=(words, letters), name="six"),
        threading.Thread(target=seven_word_solution, args=(words, letters), name="seven"),
        threading.Thread(target=eight_word_solution, args=(words, letters), name="eight"),
        threading.Thread(target=nine_word_solution, args=(words, letters), name="nine"),
        threading.Thread(target=ten_word_solution, args=(words, letters), name="ten")
    ]

    times = {}

    # Start each thread and record start times
    for thread in threads:
        times[thread.name] = timeit.default_timer()
        thread.start()

    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

        
    print("\n\n\nThese were all solutions possible with the word list.")

    



if __name__ == "__main__":
    # Example functions
    def two_word_solution(words, letters, results_2d):
        # Placeholder logic with random sleep time
        sleep_time = 1  # Random sleep time between 1 and 3 seconds
        time.sleep(sleep_time)
        results_2d.append([6])

    def three_word_solution(words, letters, results_2d):
        # Placeholder logic with random sleep time
        sleep_time = 1  # Random sleep time between 1 and 3 seconds
        time.sleep(sleep_time)
        results_2d.append([5])

    # ... (Define other functions similarly)

    # Example parameters
    words = ['word1', 'word2', 'word3']
    letters = ['a', 'b', 'c']
    results_2d = []
    # Create threads for each function with its parameters
    threads = [
        threading.Thread(target=two_word_solution, args=(words, letters, results_2d)),
        threading.Thread(target=three_word_solution, args=(words, letters, results_2d)),
        # ... (Create other threads similarly)
    ]

    # Start all threads and record start times
    times = {}
    for thread in threads:
        times[thread.name] = timeit.default_timer()
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Collect results and print elapsed times
    
    for thread in threads:
        thread_elapsed_time = timeit.default_timer() - times[thread.name]
        print(f"To find a {thread.name} word solution {thread_elapsed_time:.4f} seconds were needed.")

        
    print("All threads completed.")
