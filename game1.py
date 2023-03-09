import random

def play_hangman():
    # List of words for the game
    words = ["python", "hangman", "game", "programming", "computer"]

    # Choose a random word
    word = random.choice(words)

    # Create a list of underscores to represent the word
    guessed_word = ["_"] * len(word)

    # Set the number of guesses allowed
    num_guesses = 6

    # Loop until the word is guessed or the player runs out of guesses
    while num_guesses > 0 and "_" in guessed_word:
        # Print the current state of the word and the number of guesses remaining
        print(" ".join(guessed_word))
        print(f"You have {num_guesses} guesses remaining.")

        # Get a letter guess from the user
        guess = input("Guess a letter: ").lower()

        # Check if the letter is in the word
        if guess in word:
            # Update the guessed word with the letter
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("Correct!")
        else:
            print("Incorrect.")
            num_guesses -= 1

    # Print the final state of the word and the result of the game
    print(" ".join(guessed_word))
    if "_" not in guessed_word:
        print("Congratulations, you guessed the word!")
    else:
        print("Sorry, you ran out of guesses. The word was:", word)

if __name__ == "__main__":
    play_hangman()