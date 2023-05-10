import random
import colorama
from colorama import Fore, Style
colorama.init()

init() #Initialise colorama

def generate_word():
    words = [
        'apple', 'banana', 'cherry', 'grape', 'melon', 'peach', 'pear', 'plum',
        'table', 'chair', 'beach', 'lucky', 'prize', 'zebra', 'mouse', 'paper',
        # ... (add more words here)
    ]
    return random.choice(words)

def check_guess(word, guess):
    if len(guess) != len(word):
        return False

    correct_letters = []
    misplaced_letters = []

    for i in range(len(word)):
        if word[i] == guess[i]:
            correct_letters.append(guess[i])
        elif guess[i] in word:
            misplaced_letters.append(guess[i])

    correct_letters_str = ''.join(correct_letters)
    misplaced_letters_str = ''.join(misplaced_letters)

    feedback = [
        f'{Fore.GREEN}{char}{Style.RESET_ALL}' if char in correct_letters else
        f'{Fore.YELLOW}{char}{Style.RESET_ALL}' if char in misplaced_letters else
        f'{Fore.RED}_'
        for char in guess
    ]

    print(' '.join(feedback))
    return guess == word

def play_wordle():
    print("Welcome to Wordle!")
    print("Guess the five-letter word.")

    word = generate_word()
    attempts = 0

    while attempts < 6:
        guess = input("Enter your guess: ").lower()

        if check_guess(word, guess):
            print("Congratulations! You guessed the word.")
            return

        attempts += 1
        print(f"Attempt {attempts} out of 6")

    print("Game over! You did not guess the word.")
    print(f"The word was: {word}")

play_wordle()