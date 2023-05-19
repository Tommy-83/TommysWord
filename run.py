from flask import Flask, render_template, request, jsonify
import random
from termcolor import colored

app = Flask(__name__)

def generate_word():
    words = [
        "stove", "grape", "apple", "honey", "flame", "table", "fence", "lucky", "scent", "novel",
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

    return ' '.join(feedback)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess_input = request.form['guess']
    correct = check_guess(hidden_word, guess_input)

    response = {
        'correct': correct,
        'feedback': check_guess(hidden_word, guess_input),
        'attempts': attempts
    }

    if correct:
        response['message'] = f"Congratulations! You guessed the word '{hidden_word}' in {6 - attempts + 1} attempts."
    elif attempts == 1:
        response['message'] = f"Game over! You did not guess the word. The word was '{hidden_word}'."
    else:
        response['message'] = f"Try again. {attempts - 1} attempts remaining."

    return jsonify(response)

@app.route('/play-again', methods=['POST'])
def play_again():
    global hidden_word, attempts

    hidden_word = generate_word()
    attempts = 6

    return jsonify({'playing': True})

hidden_word = ''
attempts = 6

if __name__ == '__main__':
    app.run()
   