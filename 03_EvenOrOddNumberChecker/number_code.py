#-----------------------------------------------------------------------------
# Name:        Even or Odd Number Checker (number_code.py)
# Purpose:     Determines if a number is even or odd
#
# Author:      TA - 1034286
# Created:     26-Feb-2025
#-----------------------------------------------------------------------------

print("Even or Odd Number Checker")

# Prompt user to enter a number and convert input to an integer
number = int(input("Enter your number: "))

# Check if the number is even or odd
if number % 2 == 0:  # If the remainder when divided by 2 is 0, it's even
    print("Even")
else:
    print("Odd")  # Otherwise, it's odd