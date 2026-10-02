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

Submitting the mathematically correct answer is rejected as incorrect because operands are joined together as text instead of being calculated. Ensure the game correctly evaluates the arithmetic problem according to its active operator.

### Task 2: Implement a per-question timer bar

Players currently have unlimited time to answer each flashcard. Add a visible countdown timer bar below the active card that tracks remaining time and automatically registers a missed attempt if time runs out before submission.

### Task 3: Implement consecutive correct streak multipliers

Correct answers currently grant only a flat point increase regardless of player consistency. Introduce a streak multiplier that escalates score rewards for consecutive correct answers and resets back to baseline on any wrong answer or timeout.

### Task 4: Implement Division Operator with Clean Integer Quotients

The flashcard pool only tests addition, subtraction, and multiplication. Add integer division into card generation, ensuring that every generated problem divides evenly with whole integer answers and no remainders.

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
