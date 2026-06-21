# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!


## 📝 Document Your Experience

**Purpose:** A Streamlit number-guessing game where the player guesses a secret number between 1 and 100 within 8 attempts, getting "Too High" / "Too Low" hints until they win or run out of attempts.

**Bugs found:**
- Attempts counter ran past the 8-attempt limit and went negative ("Attempts left: -3").
- New Game didn't fully reset — old score and history stuck around and the game stayed locked on "Game over."
- Guess history stored empty strings instead of numbers when an empty input was submitted.
- Hints were backwards — a guess that was too high told the player to "Go HIGHER!" (and vice versa).

**Fixes applied:**
- Enforced the attempts limit on every submit so the game locks at exactly 8.
- Made New Game reset score, history, status, and attempts so a fresh game starts cleanly.
- Swapped the hint messages so "Too High" tells you to go LOWER and "Too Low" tells you to go HIGHER.
- Refactored check_guess and parse_guess into logic_utils.py and added a passing pytest suite.

## 📸 Demo Walkthrough


1. The game starts with a secret number between 1 and 100 and 8 attempts allowed.
2. User enters a guess of 40 → game returns "Too Low"
3. User enters a guess of 70 → game returns "Too High"
4. The guess is recorded in History and the attempts counter decreases.
5. User enters the correct number → game returns "Win" and the score updates.
6. After 8 attempts without a correct guess, the game locks with "Game over."
7. Clicking New Game resets the score, history, and attempts so a fresh game can begin.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->


## 🧪 Test Results

```
============================= test session starts ==============================
platform darwin -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
collected 9 items

tests/test_game_logic.py::test_check_guess_outcomes PASSED               [ 11%]
tests/test_game_logic.py::test_hint_messages_point_the_right_way PASSED  [ 22%]
tests/test_game_logic.py::test_wrong_guess_does_not_change_score PASSED  [ 33%]
tests/test_game_logic.py::test_first_guess_win_returns_100 PASSED        [ 44%]
tests/test_game_logic.py::test_parse_guess_rejects_non_numeric PASSED    [ 55%]
tests/test_game_logic.py::test_parse_guess_rejects_empty_input PASSED    [ 66%]
tests/test_game_logic.py::test_parse_guess_accepts_negative_number PASSED [ 77%]
tests/test_game_logic.py::test_parse_guess_truncates_decimal PASSED      [ 88%]
tests/test_game_logic.py::test_parse_guess_handles_large_number PASSED   [100%]

============================== 9 passed in 0.01s ===============================
```

## 🚀 Stretch Features

**Challenge 1 — Advanced Edge-Case Testing.** Added five `pytest` cases targeting
edge-case inputs to `parse_guess`: non-numeric strings (`"abc"`), empty input,
negative numbers (`"-7"`), decimals (`"3.9"` → truncates to `3`), and very large
numbers. All pass (see the Test Results block above). The test-generation prompts
and the rationale for each edge case are recorded in `ai_interactions.md`.
