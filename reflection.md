# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I ran the game it was clearly buggy in several ways. The attempts counter ran past the allowed limit — with "Attempts allowed: 8," I saw Attempts reach 11 and "Attempts left: -3" instead of the game ending. My guess history filled with empty strings ("") instead of numbers, and the Score stayed at 0. And after a game ended, clicking New Game didn't reset everything — the old score and history stuck around and the game stayed locked on "Game over."

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - The attempts counter went negative instead of ending the game at 8.
  - After "Game over," the New Game button left the old score and history in   place and stayed locked, so I couldn't start fresh.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Submitted guesses past the 8-attempt limit | Game ends at 8 attempts | Attempts reached 11, "Attempts left: -3" shown | none |
| Clicked Submit with the input box empty | Reject the submit without storing or counting it | Stored "" in History and still used up an attempt | Enter a guess. |
| Played to "Game over," then clicked New Game | Score resets to 0, history clears, game playable | Score stayed 5, 7 old guesses remained, still locked on "Game over" | none |


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code inside VS Code as my pair programmer for tracing bugs, refactoring, and generating a test.

Correct suggestion: When I asked it to refactor, the AI moved check_guess and parse_guess into logic_utils.py and updated the imports in app.py, and it deliberately flagged that it was leaving an unrelated string-comparison glitch untouched rather than silently changing it. This was correct — I verified by running pytest (the moved logic still returned the right High/Low/Win outcomes) and by playing the live game.

Incorrect/misleading suggestion: After generating my pytest case, the AI reported "1 passed." But it had run the test with `python -m pytest`, which quietly adds the project folder to the import path. When I ran plain `pytest` myself, it failed with "ModuleNotFoundError: No module named 'logic_utils'." So the AI's claim that the test passed was misleading for the normal way pytest is run. I caught it by running pytest directly and fixed it by adding a conftest.py at the project root so the import works either way.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed only after confirming it two ways: an automated test and live play. For the attempts-limit fix, I ran `pytest` and confirmed check_guess returns the correct outcome, then ran `streamlit run app.py` and verified the game now locks at exactly 8 attempts with "Attempts left" bottoming at 0 instead of going negative, and that New Game fully resets score and history.

The most useful test moment was the import-path failure: the test passed under `python -m pytest` but failed under plain `pytest`, which showed me my test wasn't actually wired correctly. AI helped design the test and explain why check_guess returns a tuple, but I had to verify and fix the import setup myself.


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the entire script from top to bottom every time you interact with the app — every button click or text entry triggers a full re-execution. Because of that, normal variables reset on each run, so anything that needs to persist (the secret number, score, attempts, history) has to be stored in st.session_state. Several of the bugs came from this: New Game only reset some session_state values and left others, so the old score and history carried over into the "new" game. I'd explain it to a friend as: the page redraws itself from scratch constantly, and session_state is the small memory box that survives each redraw.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is verifying AI output myself instead of trusting its report — running plain pytest caught a "passing" test that only worked under python -m pytest. Next time I'd attach the relevant files earlier and give the AI tighter, one-bug-at-a-time prompts instead of broad ones. This project changed how I think about AI-generated code: it can be confidently wrong, so I now treat its output as a draft to review and test, not a finished answer.
