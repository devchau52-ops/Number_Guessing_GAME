"""Tests for the Number Guessing Game."""

from pathlib import Path
import sys
import unittest

# Allow this file to run directly from the tests folder as well as through
# `python -m unittest discover -s tests -v` from the project root.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from number_guessing_game import calculate_score, get_valid_guess, play_round


class NumberGuessingGameTests(unittest.TestCase):
    def test_score_bands(self):
        self.assertEqual(calculate_score(1), 100)
        self.assertEqual(calculate_score(3), 100)
        self.assertEqual(calculate_score(4), 80)
        self.assertEqual(calculate_score(6), 80)
        self.assertEqual(calculate_score(7), 60)
        self.assertEqual(calculate_score(10), 60)
        self.assertEqual(calculate_score(11), 40)

    def test_invalid_guesses_are_rejected_until_a_valid_number_is_given(self):
        answers = iter(["hello", "0", "101", "42"])
        messages = []

        guess = get_valid_guess(
            input_func=lambda _prompt: next(answers),
            output_func=messages.append,
        )

        self.assertEqual(guess, 42)
        self.assertIn("Invalid entry. Please enter a whole number.", messages)
        self.assertEqual(messages.count("Please enter a number from 1 to 100."), 2)

    def test_round_reports_hints_and_returns_attempts_and_score(self):
        guesses = iter([80, 20, 42])
        messages = []

        attempts, score = play_round(
            secret_number=42,
            input_func=lambda _prompt: str(next(guesses)),
            output_func=messages.append,
        )

        self.assertEqual((attempts, score), (3, 100))
        self.assertIn("Too High!", messages)
        self.assertIn("Too Low!", messages)
        self.assertIn("Congratulations!", messages)


if __name__ == "__main__":
    unittest.main()
