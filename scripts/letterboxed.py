import json
import threading
import timeit
import time
import itertools


def is_char(c):
    if isinstance(c, str) and len(c) == 1:
        try:
            float(c)
        except ValueError:
            return True
    return False

def has_not_two_char_same_row(word, letters):
    for row in letters:
        for index, c in enumerate(word):
            if index == 0:
                continue
            if c in row and word[index-1] in row:
                return False
    return True


def two_word_solution(words, letters):
    counter = 0
    for a, b in itertools.combinations(words, 2):
        if a[-1] == b[0] and len(a) + len(b) >= 12 and {letter for letter in a} | {letter for letter in b} == letters:
            if counter == 25:                                                                                                                 ####################
                break
            GREEN = '\033[92m'
            RESET = '\033[0m'  # Reset to default color
            print(f"{GREEN}> two word solutions > possible combination > {(a,b)}{RESET}")
            counter += 1
    
def three_word_solution(words, letters):
    counter = 0
    for a, b, c in itertools.combinations(words, 3):
        if a[-1] == b[0] and b[-1] == c[0] and len(a) + len(b) + len(c) >= 12 \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} == letters:
            if counter == 25:                                                                                                                 ####################
                break
            YELLOW = '\033[93m'
            RESET = '\033[0m'  # Reset to default color
            print(f"{YELLOW}> three word solutions > possible combination > {(a,b,c)}{RESET}")
            counter += 1
    
def four_word_solution(words, letters):
    counter = 0
    for a, b, c, d in itertools.combinations(words, 4):
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and len(a) + len(b) + len(c) + len(d) >= 12 \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | {letter for letter in d} == letters:
            if counter == 25:                                                                                                                 ####################
                break
            BLUE = '\033[94m'
            RESET = '\033[0m'  # Reset to default color
            print(f"{BLUE}> four word solutions > possible combination > {(a,b,c,d)}{RESET}")
            counter += 1
            
def five_word_solution(words, letters):
    counter = 0
    for a, b, c, d, e in itertools.combinations(words, 5):
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and len(a) + len(b) + len(c) + len(d) + len(e) >= 12 \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | \
            {letter for letter in d} | {letter for letter in e} == letters:
            if counter == 25:                                                                                                                 ####################
                break
            MAGENTA = '\033[95m'
            RESET = '\033[0m'  # Reset to default color
            print(f"{MAGENTA}> five word solutions > possible combination > {(a,b,c,d,e)}{RESET}")
            counter += 1
            
def six_word_solution(words, letters):
    counter = 0
    for a, b, c, d, e, f in itertools.combinations(words, 6):
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and len(a) + len(b) + len(c) + len(d) + len(e) + len(f) >= 12 \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | \
            {letter for letter in d} | {letter for letter in e} | {letter for letter in f} == letters:
            if counter == 25:                                                                                                                 ####################
                break
            CYAN = '\033[96m'
            RESET = '\033[0m'  # Reset to default color
            print(f"{CYAN}> six word solutions > possible combination > {(a,b,c,d,e,f)}{RESET}")
            counter += 1
            
def seven_word_solution(words, letters):
    counter = 0
    for a, b, c, d, e, f, g in itertools.combinations(words, 7):
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and g[-1] == g[0] \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | \
            {letter for letter in d} | {letter for letter in e} | {letter for letter in f} | {letter for letter in g} == letters:
            if counter == 25:                                                                                                                 ####################
                break
            RED = '\033[91m'
            RESET = '\033[0m'  # Reset to default color
            print(f"{RED}> seven word solutions > possible combination > {(a,b,c,d,e,f,g)}{RESET}")
            counter += 1
            
def eight_word_solution(words, letters):
    counter = 0
    for a, b, c, d, e, f, g, h in itertools.combinations(words, 8):
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and g[-1] == g[0] and h[-1] == h[0] \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | \
            {letter for letter in d} | {letter for letter in e} | {letter for letter in f} | \
            {letter for letter in g} | {letter for letter in h} == letters:
            if counter == 25:                                                                                                                 ####################
                break
            ORANGE = '\033[38;5;208m'
            RESET = '\033[0m'  # Reset to default color
            print(f"{ORANGE}> eight word solutions > possible combination > {(a,b,c,d,e,f,g,h)}{RESET}")
            counter += 1
        
def nine_word_solution(words, letters):
    counter = 0
    for a, b, c, d, e, f, g, h, i in itertools.combinations(words, 9):
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and g[-1] == g[0] and h[-1] == h[0] and i[-1] == i[0] \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | \
            {letter for letter in d} | {letter for letter in e} | {letter for letter in f} | \
            {letter for letter in g} | {letter for letter in h} | {letter for letter in i} == letters:
            if counter == 25:                                                                                                                 ####################
                break
            PURPLE = '\033[38;5;129m'
            RESET = '\033[0m'  # Reset to default color
            print(f"{PURPLE}> nine word solutions > possible combination > {(a,b,c,d,e,f,g,h,i)}{RESET}")
            counter += 1
            
def ten_word_solution(words, letters):
    counter = 0
    for a, b, c, d, e, f, g, h, i, j in itertools.combinations(words, 10):
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and g[-1] == g[0] and h[-1] == h[0] and i[-1] == i[0] and j[-1] == j[0] \
            and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | \
            {letter for letter in d} | {letter for letter in e} | {letter for letter in f} | \
            {letter for letter in g} | {letter for letter in h} | {letter for letter in i} | {letter for letter in j}  == letters:
            if counter == 25:                                                                                                                 ####################
                break
            GRAY = '\033[38;5;240m'
            RESET = '\033[0m'  # Reset to default color
            print(f"{GRAY}> ten word solutions > possible combination > {(a,b,c,d,e,f,g,h,i,j)}{RESET}")
            counter += 1


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
        
        
        if all([is_char(i) for ii in letters for i in ii]):
            break
        
        print("\nWrong input! Input only characters.\n")
    
    
    with open("english-words/words_dictionary_letterboxed.json", "r", encoding="utf-8") as f:
        words = json.load(f)
        words = [key for key, value in words.items() if any([key.find(i) > -1 for ii in letters for i in ii])]
        words = [word for word in words if all(letter in (item for sublist in letters for item in sublist) for letter in word)]
        words = [word for word in words if has_not_two_char_same_row(word, letters)]
        
        
        
    one_word_solution = [word for word in words if {letter for letter in word} == {item for sublist in letters for item in sublist}]

    if (len(one_word_solution) == 0):
            print("Sadly there are no possible one word solutions in the word list.\n")
    
    if (len(words) in [0,1]):
            print("Sadly there are no possible words in the word list.")
            return
        

    results = {}
    
    letters = {oneletter for letter in letters for oneletter in letter}

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
