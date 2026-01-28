import random

secret_number = random.randint(1, 100)

print("🎯 Welcome to the Number Guessing Game!")
print("You have only 3 chances to guess the number between 1 and 100.")

attempts = 3

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("🎉 Congratulations! You guessed the correct number:", secret_number)
        break

    attempts -= 1
    print("Remaining chances:", attempts)

if attempts == 0:
    print("🥴 Game Over! The correct number was:", secret_number)


"sreeraj"