import random

# Predefined list of 5 words
word_list = ["python", "hangman", "coding", "robot", "laptop"]

# Randomly select a word from the list
word_to_guess = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Create a blank version of the word using underscores
display_word = ['_' for _ in word_to_guess]

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 chances to make a wrong guess.\n")

# Main game loop
while incorrect_guesses < max_attempts and '_' in display_word:
    print("Word to guess: " + ' '.join(display_word))
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try a different one.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Correct guess!\n")
        # Reveal the guessed letter in the display word
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_attempts - incorrect_guesses} tries left.\n")

# Game Over Conditions
if '_' not in display_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Game Over! The word was:", word_to_guess)
