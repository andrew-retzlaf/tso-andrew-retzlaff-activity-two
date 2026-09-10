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

BOARD_WIDTH = 15
BOARD_HEIGHT = 8
ASTEROID_TARGET = 10


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


def play_asteroid_game():
    player_x = BOARD_WIDTH // 2
    bullets = []
    asteroids = []
    score = 0
    lives = 3

    print("Destroy 10 asteroids! Use A/D to move, S to shoot, or Q to quit.")

    while lives > 0 and score < ASTEROID_TARGET:
        board = [[" " for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        board[-1][player_x] = "A"

        for bullet_x, bullet_y in bullets:
            if 0 <= bullet_y < BOARD_HEIGHT:
                board[bullet_y][bullet_x] = "|"
        for asteroid_x, asteroid_y in asteroids:
            if 0 <= asteroid_y < BOARD_HEIGHT:
                board[asteroid_y][asteroid_x] = "O"

        print(f"\nScore: {score}/{ASTEROID_TARGET} | Lives: {lives}")
        print("+" + "-" * BOARD_WIDTH + "+")
        for row in board:
            print("|" + "".join(row) + "|")
        print("+" + "-" * BOARD_WIDTH + "+")

        try:
            command = input("Your move: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

        if command == "q":
            print("You left the asteroid field.")
            return
        if command == "a":
            player_x = max(0, player_x - 1)
        elif command == "d":
            player_x = min(BOARD_WIDTH - 1, player_x + 1)
        elif command == "s":
            bullets.append((player_x, BOARD_HEIGHT - 2))
        elif command:
            print("Use A, D, S, or Q.")

        bullets = [(bullet_x, bullet_y - 1) for bullet_x, bullet_y in bullets]
        asteroids = [(asteroid_x, asteroid_y + 1) for asteroid_x, asteroid_y in asteroids]

        remaining_bullets = []
        for bullet in bullets:
            hit = next(
                (asteroid for asteroid in asteroids if asteroid == bullet),
                None,
            )
            if hit is None:
                remaining_bullets.append(bullet)
            else:
                asteroids.remove(hit)
                score += 1
        bullets = remaining_bullets

        survivors = []
        for asteroid_x, asteroid_y in asteroids:
            if asteroid_y >= BOARD_HEIGHT - 1:
                lives -= 1
            else:
                survivors.append((asteroid_x, asteroid_y))
        asteroids = survivors

        if random.random() < 0.45:
            asteroids.append((random.randrange(BOARD_WIDTH), 0))

    if score >= ASTEROID_TARGET:
        print("You cleared the asteroid field!")
    else:
        print("Game over! The asteroids got through.")


def main():
    print("Choose a game:")
    print("1. Number guessing")
    print("2. GitHub word guessing")
    print("3. Asteroid game")

    while True:
        try:
            choice = input("Enter 1, 2, or 3: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

        if choice == "1":
            play_number_game()
            return
        if choice == "2":
            play_word_game()
            return
        if choice == "3":
            play_asteroid_game()
            return

        print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()