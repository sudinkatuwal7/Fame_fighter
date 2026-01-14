# 🎯 Fame_fighter Popularity Game

---

## 📌 Overview

A fun and interactive **Python command-line game** where players compare two public figures and guess who has more social media followers. The game continues as long as the player guesses correctly and ends when they make an incorrect choice.

This project is inspired by the classic **Higher–Lower** game and focuses on strengthening Python fundamentals such as loops, conditionals, dictionaries, randomization, and clean program structure.

---

## 🚀 How the Game Works

- Two public figures (**A** and **B**) are randomly selected from a dataset
- Each figure is displayed with:
  - Name
  - Description
  - Country
- The player guesses who has more followers by typing **A** or **B**
- If the guess is correct:
  - The score increases by **1**
  - The game continues with a new comparison
- If the guess is wrong:
  - The game ends
  - The final score is displayed

---

## 🧠 Concepts Used

- `while` loops for continuous gameplay
- `if / elif / else` for decision-making
- Dictionaries for structured data storage
- `random.choice()` for random selection
- User input handling
- Score tracking logic
- Modular code using multiple Python files

---

## 📁 Project Structure

```text
higher-lower-game/
│
├── main.py        # Main game logic
├── art.py         # ASCII art (logo and VS graphic)
├── game_data.py   # Dataset of public figures
└── README.md      # Project documentation
```

---
## ▶️ How to Run the Game

1. Ensure **Python 3** is installed on your system
2. Clone this repository or download the source files
3. Open a terminal in the project directory
4. Run the game using:
   
```bash
python main.py

