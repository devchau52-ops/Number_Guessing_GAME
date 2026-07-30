# Number Guessing Game

A beginner-friendly Python console game. The program selects a random number from **1 to 100** and guides the player with `Too High` and `Too Low` hints until the number is guessed.

## Features

- Random secret number generated for every round
- Range and non-number input validation
- Attempt counter
- Score based on the number of attempts
- Replay prompt for multiple rounds in one session
- Automated test check with GitHub Actions

## Score rules

| Attempts | Score |
| --- | ---: |
| 1–3 | 100 |
| 4–6 | 80 |
| 7–10 | 60 |
| More than 10 | 40 |

## Requirements

- Python 3.10 or later

## Run the game

```bash
python number_guessing_game.py
```

On some systems, use `python3` instead of `python`.

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## Example

```text
===== Number Guessing Game =====

Guess a number between 1 and 100.

Enter your guess: 50
Too High!

Enter your guess: 25
Too Low!

Enter your guess: 37

Congratulations! You guessed the number in 3 attempts.
Your Score: 100

Do you want to play again? (Y/N): N

Thank you for playing!
```

## How the code works

1. `main()` prints the rules and starts a game round. It repeats rounds while the player answers `Y` at the replay prompt.
2. `generate_secret_number()` uses Python's built-in `random.randint()` to produce an integer from 1 through 100.
3. `get_valid_guess()` keeps asking until it receives a whole number inside that range. The `try`/`except` block catches text such as `hello`, so the program never crashes on invalid input.
4. `play_round()` compares each valid guess to the secret number, increments the attempt count, and prints `Too High`, `Too Low`, or the winning message.
5. Once the player wins, `calculate_score()` maps the attempt count to the project score rules.
6. `wants_to_play_again()` accepts only `Y` or `N`, ignoring letter case.

## Project structure

```text
.
├── .github/                     # GitHub Actions and issue templates
├── tests/                       # Automated tests
├── number_guessing_game.py      # Game source code
├── CONTRIBUTING.md              # Contribution guidance
├── CODE_OF_CONDUCT.md           # Community standards
├── LICENSE                      # MIT License
└── README.md                    # Project documentation
```

## Future ideas

- Difficulty levels with different ranges
- A timer and time-based scores
- Persistent high scores
- A graphical interface
- Multiplayer support

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

This project is available under the [MIT License](LICENSE).
