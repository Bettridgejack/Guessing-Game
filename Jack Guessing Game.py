import random

def guessing_game():
    print("Welcome to my number guessing game. have you got what it takes to guess my number?")

    target = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Please guess an integer between 1 and 100: "))
        attempts += 1

        if guess < target:
            print("Ha! You're too low! guess again.")
        elif guess > target:
            print("Mwahaha! You're too high! like a stoner!")
        else:
            print(f"Holy shit... you actually guessed it. it only took you {attempts} attempts but you guessed it!")

print(guessing_game())




