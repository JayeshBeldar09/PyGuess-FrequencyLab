# InternCircle Project 02 — Number Guessing Game & Word Counter

## Requirements
- Python 3.10 or newer
- VS Code, IDLE, or another Python editor

## Files
- `main.py`: menu, guessing game, and word counter
- `sample.txt`: example text file for testing

## Run the project
1. Extract the ZIP file.
2. Open the extracted folder in VS Code.
3. Open a terminal in that folder.
4. Run: `python main.py`
   - On some Windows systems, use: `py main.py`

## Menu
1. Play Number Guessing Game
2. Count Words in a Text File
3. Quit

## Scoring rule
The game starts at 100 points and deducts 10 points for every incorrect valid guess.
The player gets up to 7 valid guesses. Invalid inputs do not consume an attempt.
The best score is tracked for the current program session.

## Word counter
Enter `sample.txt` when prompted, or press Enter to use it by default.
The program reads UTF-8 text, ignores letter case and punctuation, and reports total words,
unique words, and the top 10 most frequent words. If the file cannot be found, it shows a
helpful message instead of crashing.

## Before submitting
- Test the game with low and high guesses, correct guesses, invalid text, and out-of-range numbers.
- Test the word counter with `sample.txt`, an empty text file, and a filename that does not exist.
- Take screenshots of one game run and one word-count run.
- Upload your code to GitHub and submit the repository link as requested by your course dashboard.
