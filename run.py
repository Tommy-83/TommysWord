import random
from colorama import init, Fore, Style

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