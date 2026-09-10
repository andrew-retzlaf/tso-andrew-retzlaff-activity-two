import random


GITHUB_TERMS = (
    "repository",
    "repo",
    "commit",
    "branch",
    "switch",
    "clone",
    "remote",
    "origin",
    "pull",
    "push",
    "merge",
    "tag",
    "pull request",
)


def play_number_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number from 1 to 100.")

    while True:
        try:
            guess_text = input("Enter your guess: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Your guess must be between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Higher!")
        elif guess > secret_number:
            print("Lower!")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            return


def play_game():
    """Keep the original entry point as an alias for number mode."""
    play_number_game()


def play_word_game():
    secret_word = random.choice(GITHUB_TERMS)
    guessed_letters = set()
    attempts = 0

    print("Guess the GitHub term one letter at a time.")

    while True:
        display = " ".join(
            character if character == " " or character in guessed_letters else "_"
            for character in secret_word
        )
        print(f"\nWord: {display}")

        if all(character == " " or character in guessed_letters for character in secret_word):
            print(f"Correct! The word was '{secret_word}'. You got it in {attempts} guesses.")
            return

        try:
            guess = input("Guess a letter: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        attempts += 1

        if guess in secret_word:
            print("Good guess!")
        else:
            print("That letter is not in the word.")


def main():
    print("Choose a game:")
    print("1. Number guessing")
    print("2. GitHub word guessing")

    while True:
        try:
            choice = input("Enter 1 or 2: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

        if choice == "1":
            play_number_game()
            return
        if choice == "2":
            play_word_game()
            return

        print("Please choose 1 or 2.")


if __name__ == "__main__":
    main()