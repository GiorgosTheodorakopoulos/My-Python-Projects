import random

a = int(input("The minimum value is: "))
b = int(input("The maximum value is: "))
number = random.randint(a, b)

max_attempts = 5
attempts = 0

try:
    guess = int(input(f"Guess a number between {a} and {b}: "))
except ValueError:
    print("Please enter a valid number")

while guess != number and attempts < max_attempts:

    attempts += 1
    if guess is not None:
            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
    if attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Guess a number between {a} and {b}: "))
        except ValueError:
            print("Please enter a valid number")
            guess = None
    else:
        break
print(f"Congrats! You guessed the number in {attempts + 1} attempts.!")
