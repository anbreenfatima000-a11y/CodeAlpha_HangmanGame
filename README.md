# CodeAlpha Hangman Game

A simple **console-based Hangman game developed in Python** as part of my **CodeAlpha Internship**.

The player has to guess the hidden word one letter at a time. The game provides a limited number of incorrect attempts and gives feedback after each guess.

## Features

* Randomly selects a word from a predefined list.
* Allows the player to guess one letter at a time.
* Validates user input to accept only a single alphabetic character.
* Prevents the same letter from being guessed multiple times.
* Displays the correctly guessed letters in their positions.
* Allows up to **6 incorrect guesses**.
* Displays a winning message when the word is guessed correctly.
* Ends the game when all incorrect attempts are used.

## Technologies Used

* **Python 3**
* `random` module

## How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository:

```bash
git clone https://github.com/your-username/CodeAlpha_HangmanGame.git
```

3. Open the project folder:

```bash
cd CodeAlpha_HangmanGame
```

4. Run the program:

```bash
python hangman_game.py
```

## How to Play

1. Run the program.
2. A hidden word will be selected randomly.
3. Enter one letter when prompted.
4. Correct guesses will reveal the letter in the word.
5. Incorrect guesses reduce the number of remaining attempts.
6. Guess the complete word before using all 6 incorrect attempts to win.

## Sample Words

The current version uses a predefined list of words, including:

* Rhythm
* Zombies
* Nature
* Genre
* Adventure

## Project Structure

```text
CodeAlpha_HangmanGame/
│
├── hangman_game.py
└── README.md
```

## Internship Task

This project was completed as part of the **CodeAlpha Python Programming Internship** to practice Python fundamentals, including:

* Variables and data types
* Lists
* Conditional statements
* Loops
* User input
* String handling
* Random selection
* Basic game logic

## Author

**Anbreen Fatima**

BS Information Technology
Python Programming Intern — CodeAlpha

