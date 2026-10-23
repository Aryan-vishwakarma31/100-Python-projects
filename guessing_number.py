
import random

# ANSI colors and text styles
BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 5

    print(f"\n{BOLD}{CYAN}================================")
    print("       NUMBER GUESSING GAME")
    print(f"================================{RESET}")
    print(f"Guess a number between 1 and 100.")
    print(f"You have {max_attempts} attempts.\n")

    for attempt in range(1, max_attempts + 1):
        print(
            f"{YELLOW}Attempt {attempt} "
            f"of {max_attempts}{RESET}"
        )

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print(f"{RED}Please enter a valid integer!{RESET}\n")
            continue

        if not 1 <= guess <= 100:
            print(f"{RED}Enter a number from 1 to 100!{RESET}\n")
            continue

        if guess == secret_number:
            print(f"\n{GREEN}{BOLD}Correct guess! You won!{RESET}")
            print(f"You guessed it in {attempt} attempt(s).")
            return

        elif guess < secret_number:
            print(f"{CYAN}Too low! Guess higher.{RESET}")
        else:
            print(f"{CYAN}Too high! Guess lower.{RESET}")

        if attempt < max_attempts:
            print(f"{YELLOW}Attempts remaining: "
                  f"{max_attempts - attempt}{RESET}\n")

    print(f"\n{RED}{BOLD}Game over!{RESET}")
    print(f"The secret number was {secret_number}.")


def main():
    while True:
        play_game()
        choice = input(
            f"\n{BOLD}Play again? (y/n): {RESET}"
        ).strip().lower()

        if choice != "y":
            print(f"\n{GREEN}Thanks for playing!{RESET}")
            break


if __name__ == "__main__":
    main()
