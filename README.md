# brute-force-some-NYTimes-games

## Overview

This Python script is a simple brute force solver for popular New York Times word games, including Letter Boxed and Wordle. The purpose of this script is to assist users in finding possible solutions to these games by systematically trying different combinations of letters.

**Note: This script is intended for educational and personal use only. Use of automated solvers may violate the terms of service of the respective games.**

## Features

- **Letter Boxed Solver:** Finds words that can be formed using the given set of letters in the Letter Boxed game.
- **Wordle Solver:** Attempts to guess the target word in the Wordle game by trying different combinations based on feedback.

## Getting Started

1. Clone this repository to your local machine.

    ```bash
    git clone [https://github.com/your-username/nytimes-games-solver.git](https://github.com/SirMrManuel0/brute-force-some-NYTimes-games.git)
    ```

2. Install the required dependencies.

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script with the desired game mode.

    ```bash
    python solver.py letterboxed
    ```

    or

    ```bash
    python solver.py wordle
    ```

## Usage

- For Letter Boxed:
  - Enter the set of letters when prompted.
  - The script will output all possible words that can be formed using the given letters.

- For Wordle:
  - Provide feedback based on the letters guessed.
  - The script will generate new guesses until the target word is found.

## Acknowledgment

This program uses the wordlist from [dwyl/english-words](https://github.com/dwyl/english-words). Check out their repository for more information and explore their other projects.

Please note that the wordlist is provided under the [Unlicense](https://github.com/dwyl/english-words/blob/master/LICENSE.md), and you should review and comply with their licensing terms.

## Disclaimer

This script is provided as-is and comes with no guarantees or warranties. Use it responsibly and in accordance with the terms of service of the respective games.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
