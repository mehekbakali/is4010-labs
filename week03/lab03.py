import random


def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    return f"The {adjective} {noun} decided to {verb} all day."


def guessing_game():
    """Run an interactive number-guessing game."""
    secret = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number from 1 to 100: "))

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct!")
            break
