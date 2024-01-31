import random


def guess_the_number(low=1, high=100):
    random_number = random.randint(low, high)
    user_guess = None

    while user_guess != random_number:
        user_guess = int(input(f"Guess a number between {low} and {high}: "))
        if user_guess < random_number:
            print("Your guess is too low. Try again!")
        elif user_guess > random_number:
            print("Your guess is too high. Try again!")
        else:
            print("Congratulations, you guessed the number correctly!")

    return random_number


random_number = guess_the_number(1, 3)
print(f"The randomly generated number was {random_number}.")
