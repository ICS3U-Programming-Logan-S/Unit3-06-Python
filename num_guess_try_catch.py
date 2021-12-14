#!/usr/bin/env python3
# Created by: Logan Sweeney
# Created on: Dec 8, 2021
# This program asks the user to guess a number
# and if they are incorrect it will tell them, and end the game.
import random
import time


def main():
    # Create the random number
    random_number = random.randint(1, 9)

    # Get number from user
    number_input = input("Guess a random number from 0-9: ")

    # Try catch statement
    try:
        # Check to see if they got the right number or wrong
        number_input_as_integer = int(number_input)
        if number_input_as_integer == random_number:
            print("Correct!!")
        elif number_input_as_integer > 9:
            print("Too high... Why would you even try that?")
        else:
            print()
            print("Incorrect... My favorite number is {}. "
                  .format(random_number))
    except Exception:
        print()
        print("This is either a number higher or lower than "
              "the range, or not even a letter! Game will now end.")
    finally:
        time.sleep(1)
        print()
        print("Thanks for guessin'!")


if __name__ == "__main__":
    main()
