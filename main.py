#   NUMBER GUESSING GAME
import random

attempts = 0
random_number = random.randint(1, 100)
print(random_number)
print("WELCOME TO THE NUMBER GUESSING GAME")
print("I'M THINKING OF A NUMBER BETWEEN 1 AND 100")
difficulty_level = input("CHOOSE A DIFFICULTY: TYPE 'EASY' OR 'HARD': ").upper()

if difficulty_level == "EASY":
    attempts = 10
elif difficulty_level == "HARD":
    attempts = 5


def decrease_attempts():
    global attempts
    attempts -= 1


def user_lose():
    if attempts == 0:
        print(f"YOU RAN OUT OF ATTEMPTS, THE ANSWER WAS {random_number}, YOU LOSE!")


print(f"YOU HAVE {attempts} REMAINING TO GUESS THE NUMBER")
while attempts != 0:
    user_guess = int(input("MAKE A GUESS: "))
    if user_guess > random_number:
        decrease_attempts()
        print("TOO HIGH")
        print(f"YOU HAVE {attempts} REMAINING TO GUESS THE NUMBER")
        user_lose()
    elif user_guess < random_number:
        decrease_attempts()
        print("TOO LOW")
        print(f"YOU HAVE {attempts} REMAINING TO GUESS THE NUMBER")
        user_lose()
    else:
        attempts = 0
        print(f"YOU GOT IT, THE ANSWER WAS {random_number}")
