import random

secret = random.randint(1, 100)

print("Guess the number between 1 and 100")

attempts = 0

guess = 0

while guess != secret:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct!")
        print("You guessed it in", attempts, "attempt(s).")
