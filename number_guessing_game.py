"""A console-based number guessing game."""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 100


def generate_secret_number():
    """Return a random whole number in the game's allowed range."""
    return random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)


def get_valid_guess(input_func=input, output_func=print):
    """Prompt until the player enters a whole number from 1 through 100."""
    while True:
        player_input = input_func(
            f"Enter your guess ({MINIMUM_NUMBER}-{MAXIMUM_NUMBER}): "
        ).strip()

        try:
            guess = int(player_input)
        except ValueError:
            output_func("Invalid entry. Please enter a whole number.")
            continue

        if MINIMUM_NUMBER <= guess <= MAXIMUM_NUMBER:
            return guess

        output_func(
            f"Please enter a number from {MINIMUM_NUMBER} to {MAXIMUM_NUMBER}."
        )


def calculate_score(attempts):
    """Return the score earned for a completed round."""
    if attempts <= 3:
        return 100
    if attempts <= 6:
        return 80
    if attempts <= 10:
        return 60
    return 40


def play_round(secret_number=None, input_func=input, output_func=print):
    """Play one round and return its number of attempts and score."""
    if secret_number is None:
        secret_number = generate_secret_number()

    attempts = 0
    output_func("")
    output_func(f"Guess a number between {MINIMUM_NUMBER} and {MAXIMUM_NUMBER}.")

    while True:
        guess = get_valid_guess(input_func, output_func)
        attempts += 1

        if guess > secret_number:
            output_func("Too High!")
        elif guess < secret_number:
            output_func("Too Low!")
        else:
            score = calculate_score(attempts)
            attempt_word = "attempt" if attempts == 1 else "attempts"
            output_func("")
            output_func("Congratulations!")
            output_func(f"You guessed the number in {attempts} {attempt_word}.")
            output_func(f"Your Score: {score}")
            return attempts, score


def wants_to_play_again(input_func=input, output_func=print):
    """Ask for a Y/N response and return True only for Y."""
    while True:
        answer = input_func("\nDo you want to play again? (Y/N): ").strip().lower()

        if answer == "y":
            return True
        if answer == "n":
            return False

        output_func("Please enter Y for yes or N for no.")


def main():
    """Run the game until the player chooses not to replay."""
    print("===== Number Guessing Game =====")
    print("\nRules:")
    print("- Guess the secret whole number between 1 and 100.")
    print("- Each guess receives a Too High or Too Low hint.")
    print("- Fewer attempts earn a higher score.")

    while True:
        play_round()
        if not wants_to_play_again():
            break

    print("\nThank you for playing!")


if __name__ == "__main__":
    main()
