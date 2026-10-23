"""
InternCircle Project 02: Number Guessing Game & Word Counter
Python 3.10+
"""

import random
import string
from collections import Counter
from pathlib import Path

MAX_ATTEMPTS = 7
STARTING_SCORE = 100
POINTS_PER_WRONG_GUESS = 10


def play_game():
    """Play a number guessing game and return the score (0 if not won)."""
    best_score = 0

    while True:
        secret_number = random.randint(1, 100)
        attempts = 0
        score = STARTING_SCORE
        won = False

        print("\n=== NUMBER GUESSING GAME ===")
        print("I'm thinking of a number from 1 to 100.")
        print(f"You have {MAX_ATTEMPTS} attempts.")
        print(f"Score starts at {STARTING_SCORE}; each wrong guess costs "
              f"{POINTS_PER_WRONG_GUESS} points.")

        while attempts < MAX_ATTEMPTS:
            raw_guess = input(f"\nAttempt {attempts + 1}/{MAX_ATTEMPTS} - Enter a number: ").strip()

            try:
                guess = int(raw_guess)
            except ValueError:
                print("Please enter a whole number, such as 42.")
                continue

            if not 1 <= guess <= 100:
                print("Your guess must be between 1 and 100.")
                continue

            attempts += 1

            if guess == secret_number:
                won = True
                print("Correct! You guessed the number.")
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")

            score = max(0, score - POINTS_PER_WRONG_GUESS)
            print(f"Current score: {score}")

        if won:
            print(f"\nYou won in {attempts} valid guess(es)!")
            print(f"Your score: {score}")
            if score > best_score:
                best_score = score
                print("New best score!")
        else:
            score = 0
            print(f"\nNo attempts left. The number was {secret_number}.")
            print("Your score: 0")

        print(f"Best score this session: {best_score}")
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            return


def count_words(path_text):
    """Read a text file and return its word-frequency Counter, or None on error."""
    path = Path(path_text)

    try:
        with path.open("r", encoding="utf-8") as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"File not found: {path}")
        print("Check the filename and make sure the file is in the project folder.")
        return None
    except OSError as error:
        print(f"Could not read the file: {error}")
        return None

    # Remove punctuation, then split the cleaned text into words.
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return Counter(words)


def word_counter_tool():
    """Ask for a filename and display word-frequency statistics."""
    print("\n=== TEXT FILE WORD COUNTER ===")
    print("Tip: Put your .txt file in the same folder as main.py.")
    path = input("Enter text filename (default: sample.txt): ").strip()
    if not path:
        path = "sample.txt"

    counts = count_words(path)
    if counts is None:
        return

    total_words = sum(counts.values())
    unique_words = len(counts)

    print("\n--- WORD COUNT RESULTS ---")
    print(f"Total words : {total_words}")
    print(f"Unique words: {unique_words}")

    if not counts:
        print("The file is empty or contains no words.")
        return

    print("\nTop 10 most common words")
    print(f"{'Word':<20}{'Count':>8}")
    print("-" * 28)
    for word, count in counts.most_common(10):
        print(f"{word:<20}{count:>8}")


def main():
    """Display the main menu until the user chooses to quit."""
    while True:
        print("\n" + "=" * 38)
        print(" PYTHON PROJECT 02")
        print(" Number Guessing Game & Word Counter")
        print("=" * 38)
        print("1. Play Number Guessing Game")
        print("2. Count Words in a Text File")
        print("3. Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            word_counter_tool()
        elif choice == "3":
            print("Thanks for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
