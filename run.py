import random
from termcolor import colored

def generate_word():
    words = ["stove", "grape", "apple", "honey", "flame", "table", "fence", "lucky", "scent", "novel",
"chess", "frost", "wrist", "juice", "waste", "virus", "sweep", "beard", "shaft", "shock",
"brick", "beast", "sight", "curse", "treat", "charm", "yield", "frown", "horse", "spoil",
"bless", "bonus", "queen", "river", "sweat", "braid", "grasp", "blend", "cliff", "crane",
"shelf", "doubt", "rider", "bunch", "nurse", "vital", "tiger", "trick", "wool", "cabin",
"flash", "sweep", "grill", "drain", "blame", "sting", "curve", "lemon", "spear", "steak",
"wrist", "plaza", "prize", "swamp", "glory", "stool", "angel", "ocean", "black", "stair",
"shirt", "chair", "craft", "shade", "steel", "roast", "order", "proud", "thief", "broom"
 ]
    five_letter_words = [word for word in words if len(word) == 5]
    return random.choice(five_letter_words)

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

    while True:
        word = generate_word()
        attempts = 0
        guessed_words = []

        while attempts < 6:
            guess = input("Enter your guess: ").lower()
            guessed_words.append(guess)

            if check_guess(word, guess):
                print("Congratulations! You guessed the word.")
                break

            attempts += 1
            print(f"Attempt {attempts} out of 6")

        if attempts == 6:
            print("Game over! You did not guess the word.")
            print(f"The word was: {word}")

        print("\nGuessed Words:")
        for word in guessed_words:
            print(word)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

play_wordle()
