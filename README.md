# Wordle Game

Wordle is a word guessing game where the player tries to guess a five-letter word within six attempts. The game provides feedback for each guess, indicating correct letters in the correct positions (marked as green), letters that exist in the word but in the wrong positions (marked as yellow), and letters that are not in the word (marked as red).

## Requirements

- Python 3.x
- termcolor package (install using `pip install termcolor`)

## How to Play

1. Clone the repository or download the source code.
2. Install the termcolor package using `pip install termcolor`.
3. Run the `wordle.py` file using Python: `python wordle.py`.
4. The game will start, and you will be prompted to enter your guesses.
5. Guess the five-letter word within six attempts.
6. For each guess, the feedback will be displayed, indicating correct and misplaced letters.
7. After six attempts, the game will end, and the correct word will be revealed.
8. You will have the option to play again or exit.

##Game flow:

##Start
*Generate a random 5-letter word
*Set attempts = 0
*Set guessed_words = []

###Loop while attempts < 6
│1. Display "Enter your guess:"
│   *Read player's guess
│    *Add guess to guessed_words
│       **If guess is correct
│   │    **Display "Congratulations! You guessed the word."
│   │      **Break out of the loop
│   ├─ Increment attempts by 1
│   ├─ Display "Attempt x out of 6"
│   └─ If attempts = 6
│       ├─ Display "Game over! You did not guess the word."
│       └─ Display "The word was: <word>"
└─ Display "Guessed Words:"
    └─ Loop through guessed_words and display each word
    └─ Ask player if they want to play again
        ├─ If player chooses to play again
        │   └─ Go back to Start
        └─ If player chooses to exit
            └─ End



