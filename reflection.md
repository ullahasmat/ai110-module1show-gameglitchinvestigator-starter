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

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
