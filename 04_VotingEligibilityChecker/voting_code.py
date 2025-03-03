#-----------------------------------------------------------------------------
# Name:        Voting Eligibility Checker (voting_code.py)
# Purpose:     Determines if a user is eligible to vote
#
# Author:      TA - 1034286
# Created:     26-Feb-2025
#-----------------------------------------------------------------------------

print("Voting Eligibility Checker")

# Prompt user to enter age and convert input to an integer
age = int(input("How old are you? "))

# Check voting eligibility based on age
if 17 >= age >= 0:  # If age is between and including 0 and 17, the person can not vote
    print("Sorry, you are not eligible for voting")
elif 99 >= age >= 18:  # If age is between 18 and 99, the person can vote
    print("You are eligible for voting")
else:
    print("Invalid")   # Negative numbers or unrealistic values