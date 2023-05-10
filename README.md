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

## Testing

The Wordle game was tested to ensure its functionality. The following areas were tested:

- **Guess Validation**: Test that the game correctly validates the length of the guess and rejects guesses that are not five letters long.
- **Feedback Generation**: Test that the game generates the appropriate feedback based on the guess and the target word.
- **Winning Condition**: Test that the game correctly identifies when the player has guessed the word and ends the game.
- **Losing Condition**: Test that the game correctly ends after six unsuccessful attempts and reveals the correct word.
- **Play Again Option**: Test that the game allows the player to play again or exit after each game.

## Deployment

### The project was deployed using Code Institutes mock terminal for Heroku.

### Steps to deploy:
* Fork or clone this repository.
* Ensure the Procfile is in place.
  requirements.txt can be left empty as this project does not use any external libraries.
* Create a new app in Heroku.
* Select "New" and "Create new app".
* Name the new app and click "Create new app".
* In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list).
* Whilst still in "Settings", click "Reveal Config Vars" and input the folloing. KEY: PORT, VALUE: 8000. Nothing else is needed here as this 
  project does not have any sensitive files.
* Click on "Deploy" and select your deploy method and repository.
* Click "Connect" on selected repository.
* Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section.
* Heroku will now deploy the site.




