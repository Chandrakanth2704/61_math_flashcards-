# Math Flashcards Repair Lab

This project is an interactive mental arithmetic flashcard game using **Pygame**. It introduces students to mathematical operation parsing, string formatting vs arithmetic evaluation, custom text-box input components, and feedback messaging within an object-oriented codebase.
---

## What's Provided

A working Math Flashcards game with:

- Dynamic flashcard generation featuring randomized operands and operators (`+`, `-`, `*`)
- Subtraction safety logic preventing negative outcomes during card generation
- A custom numeric `TextBox` widget supporting cursor input, digit entry, and backspace
- Input submission via the `Return` / `Enter` key or clicking the `SUBMIT` button
- Live score and attempt tracking with color-coded feedback messages

It has **one deliberate bug** and **three optional features** left as tasks to implement. You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional and more interesting.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**
---

## Getting Started

### Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install pygame
```

3. Run the game:

```bash
python main.py
```

**Controls:** Type numeric digits into the text box and press Return (or click SUBMIT) to submit your answer


## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Fix the string concatenation calculation bug

Entering the mathematically correct answer is judged as incorrect by the game. In game_engine.compute_expected_answer(), the function returns int(f"{self.num_a}{self.num_b}") instead of evaluating the actual arithmetic operation. For example, 7 + 5 expects 75 rather than 12. Refactor compute_expected_answer() to check self.operator and compute the correct mathematical result using +, -, or *.

### Task 2: Implement a per-question timer bar

Flashcards are more engaging when speed is tested. Add a visible countdown timer bar (e.g., 10 seconds) below the card container in game_engine.render(). Update the timer in game_engine.update(), and if the time runs out before the player submits, automatically count the card as an incorrect attempt, display a "TIME'S UP!" warning, and move to the next card.

### Task 3: Implement consecutive correct streak multipliers

Currently, every correct answer simply awards a flat +1 point. Implement a consecutive streak tracker in game_engine. Maintain a multiplier that increases for every consecutive correct response (e.g., 2x score for 3 in a row, 3x score for 5 in a row), and reset the streak counter to zero on any incorrect answer or timeout.

### Task 4: Implement division operator support with integer results

Flashcards only test addition, subtraction, and multiplication. Add the integer division operator (/) into game_engine.generate_new_card(). Ensure that cards generated with division always produce clean whole numbers without remainders (for example, by generating a divisor and quotient first, then multiplying them to produce the dividend).
---

## Expected Behavior

- Flashcards present arithmetic problems with random numbers and operators.
- Typing the correct arithmetic answer increments the score and moves to the next card.
- Submitting an incorrect answer displays the expected value and clears the input box for retry or tracking.
- Submitting an empty input box prompts the user without counting as a failed attempt.
---

## Folder Structure

```
math_flashcards/
├── game/
│   ├── game_engine.py
│   └── text_box.py
├── main.py
└── README.md
```

## Submission Checklist

Submission is only the following three things:

- [] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [] The Chat/LLM used page link, with the complete chat history
