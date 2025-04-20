import random

def guessing_game():
    number_to_guess = random.randint(1, 10) 
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 10")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")


guessing_game()
