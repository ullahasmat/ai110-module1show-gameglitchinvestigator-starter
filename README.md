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

**Fixes applied:**
- Enforced the attempts limit on every submit so the game locks at exactly 8.
- Made New Game reset score, history, status, and attempts so a fresh game starts cleanly.
- Refactored check_guess and parse_guess into logic_utils.py and added a passing pytest case.

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

​```
============================= test session starts =============================
collected 1 item
tests/test_game_logic.py .                                              [100%]
============================== 1 passed in 0.01s ==============================
​```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
