import random

# Generate a random number between 1 and 100 (incremented by 10)
secret_number = random.randint(1,20)
attempts = 10

print("Welcome to Guess the Number!")
print(f"A random number had been selected from 1-20")
print(f"You have {attempts} attempts to guess it correctly.")

win = False
while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print(f"Congratulations! You've guessed the correct number: {secret_number}")
        win = True
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    attempts -= 1

if win == False and attempts == 0:
    print(f"Sorry, you ran out of guesses. THe correct number was:  {secret_number}")