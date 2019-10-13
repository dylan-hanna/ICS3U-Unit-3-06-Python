#!usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Sept 2019
# This program runs the number guessing game


import random


def main():

    random_number = (1, 20+1)
    integer_as_string = input("Enter your prediction between 1 and 20: ")
    print("")

    try:
        integer_as_number = int(integer_as_string)
        if integer_as_string == random_number:
            print("Correct! {} was the right number".format(integer_as_string))
        else:
            print("{} is not the right number!".format(integer_as_string))
    except Exception:
            print("{} is not an integer".format(integer_as_string))
    finally:
            print("")
            print("")
            print("Thanks for playing")


if __name__ == "__main__":
        main()
