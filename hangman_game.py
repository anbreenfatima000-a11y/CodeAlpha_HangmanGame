import random

words_list = ["Rhythm", "Zombies", "Nature", "Genre", "Adventure"]

word = random.choice(words_list)
selected_word = word.lower()
word_length = len(selected_word)

print("\t\t__________________________________")
print("\n\t\t     WELCOME TO HANGMAN GAME!  ")
print("\t\t     (The word guessing game)")
print("\t\t__________________________________")

dashes = ["_"] * word_length
print("\nWord : " + " " .join(dashes), end=" ")
print("\nincorrect guesses = 6")

incorrect_guesses = 0
user_guesses = []
while True:
    guess = input("\n\nGuess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in user_guesses:
        print("You've already guessed that letter!")
        continue
    user_guesses.append(guess)
    if guess in selected_word:
        for index, letter in enumerate(selected_word):
            if letter == guess:
                dashes[index] = guess.upper()
        print("Correct guess!")
        print("\nWord : " + " " .join(dashes), end=" ")
        if "_" not in dashes:
            print("\nCongratulations! You've guessed the word correctly :", selected_word.upper())
            break      
    else:
        incorrect_guesses += 1
        print("Incorrect guess! You have", 6 - incorrect_guesses, "guesses left.")
        if incorrect_guesses >= 6:
            print("\nGame Over! The correct word was:", selected_word)
            break

