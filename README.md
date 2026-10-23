# **🎯 Terminal Number Guessing Game**

A polished, feature-rich command-line Number Guessing Game written in Python. It features colorful ANSI terminal text styling, attempt tracking with a strict limit, error handling for invalid inputs, and a continuous replay loop.

---

## **✨ Features**

* **ANSI Color Styling:** Eye-catching terminal output using bold text and colors for alerts, prompts, and success messages.
* **Attempt Tracking:** Limits players to 5 attempts per round to increase the challenge.
* **Input Validation:** Gracefully handles non-integer entries and out-of-range guesses (1–100) without crashing.
* **Replay Loop:** Option to instantly play another round or exit gracefully after a game ends.
* **Zero Dependencies:** Built completely using Python's standard library.

---

## **🚀 Getting Started**

### **Prerequisites**

Ensure you have Python 3.x installed on your system. You can verify your installation by running:

python --version

### **Installation & Execution**

1. Clone the repository:

git clone https://github.com/Aryan-vishwakarma31/100-Python-projects.git

2. Navigate to the repository folder:

cd 100-Python-projects

3. Run the game:

python guessing_number.py

---

## **🕹️ How to Play**

1. Run the script in your terminal.
2. The game will randomly choose a secret number between 1 and 100.
3. You will have 5 attempts to guess the number. Type your guess when prompted and press Enter.
4. Read the clues:
   * 📉 Too low! Guess higher.
   * 📈 Too high! Guess lower.
5. Guess the correct number before your attempts run out to win! When the round ends, you can choose to play again (y/n).

---

## **🛠️ Tech Stack & Concepts**

* **Language:** Python
* **Modules:** random
* **Core Concepts:** 
  * while and for loops
  * Conditional branching (if-elif-else)
  * Exception handling (try-except for ValueError)
  * ANSI escape sequences for text styling

---


## **📝 License**

This project is open-source and available under the MIT License.

---

Made with ❤️ by Aryan Vishwakarma
