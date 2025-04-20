def guess_game():
    secret_number = 25
    attempts= 5

    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 50.")

    while attempts >0:
        try:
            guess = int(input(f"You have {attempts} attempts left.Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if guess == secret_number:
            print("Congratulations! You guessed the number correctly.")
            break
        elif guess < secret_number:
            print("Too Low! Try a higher number.")
        else:
            print("Too High! Try a lower number.")

        attempts-= 1
    if attempts == 0:
        print(f"Sorry, you're out of attempts.The correct number was {secret_number}.")