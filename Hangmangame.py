import random

# Step 1: Predefined word list
word_list = ['apple', 'chair', 'plant', 'green', 'house']
secret_word = random.choice(word_list)

# Step 2: Initialize game state
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

# Step 3: Game loop
while True:
    # Show word progress
    display_word = ''
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    print("\nWord:", display_word.strip())
    print("Guessed letters:", ' '.join(guessed_letters))

    # Check for win
    if all(letter in guessed_letters for letter in secret_word):
        print("\U0001F389 Congratulations! You guessed the word!")
        break

    # Check for loss
    if wrong_guesses >= max_guesses:
        print("\u274C You lost! The word was:", secret_word)
        break

    # Ask user for a guess
    guess = input("Guess a letter: ").lower()

    # Validate guess
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess in word
    if guess in secret_word:
        print("\u2705 Correct!")
    else:
        print("\u274C Wrong!")
        wrong_guesses += 1
        print(f"Remaining wrong guesses: {max_guesses - wrong_guesses}")
