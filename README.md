# The Overly Verbose GPA Calculator

A tiny interactive Python script that calculates your GPA on a 4.0 scale and responds with some (very) chatty messages.

This repository contains a single script, `main.py`, that prompts you for how many classes you're taking, asks for each class grade (on a 4.0 scale), computes the average GPA, prints an encouraging (or blunt) message, and then offers to run again.

## Requirements

- Python 3.7+ (any modern Python 3 release will work)

## Usage

1. Run the script from the command line:

```bash
python3 main.py
```

2. Follow the prompts:
- Enter the number of classes (integer).
- For each class, enter a grade as a number on the 4.0 scale (e.g., 3.7, 4.0, 2.5).

The script validates that each entered grade is not greater than 4.0 — if a grade above 4 is entered it will prompt you for that class's grade again.

After calculating the average, the script prints your average GPA and a short message based on that average, then asks if you want to check again (Y/N).

## Example Session

User input is shown after the prompts.

```
Salutations fine shyt! I hope you have had a splendiferous day!
How many classes are you taking?: 3
Alright! Now please input your grade for each on a 4 point scale
Grade for class 1: 3.7
Grade for class 2: 4.0
Grade for class 3: 3.3
Thank you so much jit! I'll get right on it
Your average GPA is: 3.6666666666666665
Almost there!
Just a couple higher grades and it could be great!
Want to check again?(Y/N): N

Process finished.
```

## Implementation notes

- File: `main.py`
	- Uses a global list `gpaList` to collect grades.
	- `gpaAsk(num)` collects `num` grades from the user, re-prompting if a grade > 4.0 is entered.
	- `gpaAvg()` computes the average by summing `gpaList` and dividing by its length.
	- `again(ans)` asks whether to run the program again — accepts `Y` or `N` (case-insensitive).

## Caveats and suggested improvements

- The script assumes valid numeric input for counts and grades. Non-numeric input will raise a ValueError; adding try/except and re-prompting would improve robustness.
- The program uses a global `gpaList`. Refactoring to pass lists as function arguments would make the code cleaner and easier to test.
- The user-facing text is intentionally verbose and colloquial. If you prefer a more neutral tone, update the print statements in `main.py`.
- Add unit tests for `gpaAvg()` and refactor input collection so it can be tested without interactive stdin.

## License

This is sample code for personal use. No license is specified — add one if you plan to share or distribute it publicly.

## Contact / Next steps

- If you'd like, I can: add input validation, refactor to remove globals, or add a small test suite and CI workflow. Tell me which you'd like and I'll implement it.

