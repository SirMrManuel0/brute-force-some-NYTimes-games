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
    combinations = [
        (a, b)
        for a, b in itertools.combinations(words, 2)
        if a[-1] == b[0] and len(a) + len(b) >= 12
        and {letter for letter in a} | {letter for letter in b} == letters
    ]
    
    for combination in combinations:
        print(f"> two word solutions > possible combination > {combination}")
    
def three_word_solution(words, letters):
    combinations = [
        (a, b, c) 
        for a, b, c in itertools.combinations(words, 3)
        if a[-1] == b[0] and b[-1] == c[0] and len(a) + len(b) + len(c) >= 12
        and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} == letters
    ]
    
    for combination in combinations:
        print(f"> three word solutions > possible combination > {combination}")
    
def four_word_solution(words, letters):
    combinations = [
        (a, b, c, d)
        for a, b, c, d in itertools.combinations(words, 4)
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and len(a) + len(b) + len(c) + len(d) >= 12
        and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | {letter for letter in d} == letters
    ]
    
    for combination in combinations:
        print(f"> four word solutions > possible combination > {combination}")
            
def five_word_solution(words, letters):
    combinations = [
        (a, b, c, d, e)
        for a, b, c, d, e in itertools.combinations(words, 5)
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and len(a) + len(b) + len(c) + len(d) + len(e) >= 12
        and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | 
        {letter for letter in d} | {letter for letter in e} == letters
    ]
    
    for combination in combinations:
        print(f"> five word solutions > possible combination > {combination}")
            
def six_word_solution(words, letters):
    combinations = [
        (a, b, c, d, e, f) 
        for a, b, c, d, e, f in itertools.combinations(words, 6) 
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and len(a) + len(b) + len(c) + len(d) + len(e) + len(f) >= 12
        and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | 
        {letter for letter in d} | {letter for letter in e} | {letter for letter in f} == letters
    ]
    
    for combination in combinations:
        print(f"> six word solutions > possible combination > {combination}")
            
def seven_word_solution(words, letters):
    combinations = [
        (a, b, c, d, e, f, g) 
        for a, b, c, d, e, f, g in itertools.combinations(words, 7) 
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and g[-1] == g[0]
        and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | 
        {letter for letter in d} | {letter for letter in e} | {letter for letter in f} | {letter for letter in g} == letters
    ]
    
    for combination in combinations:
        print(f"> seven word solutions > possible combination > {combination}")
            
def eight_word_solution(words, letters):
    combinations = [
        (a, b, c, d, e, f, g, h) 
        for a, b, c, d, e, f, g, h in itertools.combinations(words, 8) 
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and g[-1] == g[0] and h[-1] == h[0]
        and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | 
        {letter for letter in d} | {letter for letter in e} | {letter for letter in f} | 
        {letter for letter in g} | {letter for letter in h} == letters
    ]
    
    for combination in combinations:
        print(f"> eight word solutions > possible combination > {combination}")
        
def nine_word_solution(words, letters):
    combinations = [
        (a, b, c, d, e, f, g, h, i) 
        for a, b, c, d, e, f, g, h, i in itertools.combinations(words, 9) 
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and g[-1] == g[0] and h[-1] == h[0] and i[-1] == i[0]
        and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | 
        {letter for letter in d} | {letter for letter in e} | {letter for letter in f} | 
        {letter for letter in g} | {letter for letter in h} | {letter for letter in i} == letters
    ]
    
    for combination in combinations:
        print(f"> nine word solutions > possible combination > {combination}")
            
def ten_word_solution(words, letters):
    combinations = [
        (a, b, c, d, e, f, g, h, i, j) 
        for a, b, c, d, e, f, g, h, i, j in itertools.combinations(words, 10) 
        if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0] and d[-1] == e[0] and e[-1] == f[0] and g[-1] == g[0] and h[-1] == h[0] and i[-1] == i[0] and j[-1] == j[0]
        and {letter for letter in a} | {letter for letter in b} | {letter for letter in c} | 
        {letter for letter in d} | {letter for letter in e} | {letter for letter in f} | 
        {letter for letter in g} | {letter for letter in h} | {letter for letter in i} | {letter for letter in j}  == letters
    ]
    
    for combination in combinations:
        print(f"> ten word solutions > possible combination > {combination}")


def index():
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
        
        
        """
    )
    
    
    while True:
        #letters = (
        #        (input("1: ").lower(), input("2: ").lower(), input("3: ").lower()), 
        #        (input("4: ").lower(), input("5: ").lower(), input("6: ").lower()), 
        #        (input("7: ").lower(), input("8: ").lower(), input("9: ").lower()),
        #        (input("10: ").lower(), input("11: ").lower(), input("12: ").lower())
        #    )
        
        
        letters = (
            ("i", "y", "a"),
            ("b", "k", "m"),
            ("h", "e", "l"),
            ("t", "c", "o")
        )
        
        
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

    # Collect results and print elapsed times
    
    for thread in threads:
        thread_elapsed_time = timeit.default_timer() - times[thread.name]
        print(f"To find a {thread.name} word solution {thread_elapsed_time:.4f} seconds were needed.")

        
    print("All threads completed.")

    



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
