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

## Game flow:

```mermaid
graph LR
    A((Start)) --> B[Generate a random 5-letter word]
    B --> C[Set attempts = 0]
    C --> D[Set guessed_words = []]
    D --> E{attempts < 6}
    E -- Yes --> F[Display "Enter your guess:"]
    F --> G[Read player's guess]
    G --> H[Add guess to guessed_words]
    H --> I{guess is correct?}
    I -- Yes --> J[Display "Congratulations! You guessed the word."]
    J --> K[Break out of the loop]
    I -- No --> L[Increment attempts by 1]
    L --> M[Display "Attempt x out of 6"]
    M --> N{attempts = 6}
    N -- Yes --> O[Display "Game over! You did not guess the word."]
    O --> P[Display "The word was: <word>"]
    P --> Q[Display "Guessed Words:"]
    Q --> R[Loop through guessed_words and display each word]
    R --> S[Ask player if they want to play again]
    S -- Yes --> A
    S -- No --> T((End))




