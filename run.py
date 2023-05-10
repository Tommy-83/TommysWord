import random
from termcolor import colored

def generate_word():
    words = ['apple', 'banana', 'cherry', 'grape', 'melon', 'peach', 'pear', 'plum']
    return random.choice(words)

def check_guess(word, guess):
    if len(guess) != len(word):
        return False

    feedback = []
    correct_letters = 0

    for i in range(len(word)):
        if word[i] == guess[i]:
            feedback.append(colored(word[i], 'green'))
            correct_letters += 1
        elif guess[i] in word:
            feedback.append(colored(guess[i], 'yellow'))
        else:
            feedback.append(colored('_', 'red'))

    print(' '.join(feedback))

    if correct_letters == len(word):
        return True

    return False

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
