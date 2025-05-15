#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 14, 2025
# This program is a calculator that allows the user
# to enter a sign, a first number, and a second number
# to perform a variety of operations (+, -, *, /, %).


# Define a function to calculate the mathematical
# operation performed on two numbers.
def calculate(sign, first_number, second_number):
    # Initialize the calculator result to zero to be used later.
    calculator_result = 0

    # Check if the user wanted to perform addition.
    if sign == "+":
        # Set the calculator result to the sum of the two numbers.
        calculator_result = first_number + second_number
    # Otherwise, check if the user wanted to perform subtraction.
    elif sign == "-":
        # Set the calculator result to the
        # difference of the two numbers.
        calculator_result = first_number - second_number
    # Otherwise, check if the user wanted to perform multiplication.
    elif sign == "*":
        # Set the calculator result to the
        # product of the two numbers.
        calculator_result = first_number * second_number
    # Otherwise, check if the user wanted to perform division.
    elif sign == "/":
        # Set the calculator result to the
        # quotient of the two numbers.
        calculator_result = first_number / second_number
    # Otherwise, the only other option is to perform modulo.
    else:
        # Set the calculator result to the
        # remainder of the two numbers.
        calculator_result = first_number % second_number

    # Return the result of the calculator after performing
    # the desired operation.
    return calculator_result


# Define the main function.
def main():
    # Display the introduction to the program.
    print("\nThis program will perform calculations between two numbers.")

    # Get the mathematical operation from the user.
    user_sign = input("\nEnter the operation you want to perform (+, -, *, /, %): ")

    # Before proceeding, check if the entered sign was +, -, *, /, or %.
    if (
        (user_sign == "+")
        or (user_sign == "-")
        or (user_sign == "*")
        or (user_sign == "/")
        or (user_sign == "%")
    ):
        # Continue and get the user's first number as a string.
        user_first_number_str = input("\nEnter the first number: ")
        # Try to validate the user's first number.
        try:
            # Attempt to convert the user's first number into a float.
            user_first_number_float = float(user_first_number_str)
            # Get the user's second number as a string.
            user_second_number_str = input("\nEnter the second number: ")
            # Try to validate the user's second number.
            try:
                # Attempt to convert the user's second number into a float.
                user_second_number_float = float(user_second_number_str)
                # Check if the user entered / or % for the sign
                # and their second number equals zero.
                if ((user_sign == "/") or (user_sign == "%")) and (
                    user_second_number_float == 0
                ):
                    # Display to the user that the result is
                    # undefined since the divisor cannot be zero.
                    # Use general formatting for readability.
                    print(
                        f"\nThe result of {user_first_number_float:g} "
                        f"{user_sign} {user_second_number_float:g} is undefined."
                    )
                # Otherwise, the answer will be valid and not undefined.
                else:
                    # Assign the calculator function with the sign
                    # and numbers to the user result variable.
                    user_result = calculate(
                        user_sign, user_first_number_float, user_second_number_float
                    )
                    # Display the result to the user with general formatting for readability.
                    print(
                        f"\nThe result of {user_first_number_float:g} "
                        f"{user_sign} {user_second_number_float:g} is {user_result:g}."
                    )
            # Runs if float() could not convert the
            # user's second number into a float.
            except ValueError:
                # Display to the user that their second number is not a valid number.
                print(f"\n{user_second_number_str} is not a valid number.")
        # Runs if float() could not convert the
        # user's first number into a float.
        except ValueError:
            # Display to the user that their first number is not a valid number.
            print(f"\n{user_first_number_str} is not a valid number.")
    # Otherwise, the user entered an unknown operation.
    else:
        # Display to the user that their entered operation is unrecognized.
        print(f"\n{user_sign} is not a recognized operation.")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
