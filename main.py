import random


def play_game():
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


if __name__ == "__main__":
    play_game()