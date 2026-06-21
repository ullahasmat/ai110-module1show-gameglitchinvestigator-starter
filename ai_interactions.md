# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

**Prompt used:** "Identify three or more edge-case inputs that could still break
`parse_guess` (non-numeric strings, negative numbers, decimals, empty input,
very large values) and generate passing pytest cases for each in
`tests/test_game_logic.py`."

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Non-numeric string | "test that `parse_guess` rejects `'abc'`" | `parse_guess("abc") == (False, None, "That is not a number.")` | ✅ Pass | A player can fat-finger letters; the game must reject them, not crash with a `ValueError`. |
| Empty input | "test the empty-box case" | `parse_guess("") == (False, None, "Enter a guess.")` | ✅ Pass | Clicking Submit with nothing typed should be rejected cleanly, not parsed as a number. |
| Negative number | "test a negative like `'-7'`" | `parse_guess("-7") == (True, -7, None)` | ✅ Pass | Negatives are out of range but should still parse without erroring, so the game logic—not the parser—decides they're wrong. |
| Decimal | "test `'3.9'`" | `parse_guess("3.9") == (True, 3, None)` | ✅ Pass | Decimals must truncate to an int via `int(float(...))` rather than raising. |
| Very large number | "test a huge value" | `parse_guess("1000000000") == (True, 1000000000, None)` | ✅ Pass | Python ints are unbounded, so large inputs shouldn't overflow or crash. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
