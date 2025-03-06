#-----------------------------------------------------------------------------
# Name:        Student Grading System (grade_code.py)
# Purpose:     Determines the grade based on a student's score
#
# Author:      TA - 1034286
# Created:     26-Feb-2025
#-----------------------------------------------------------------------------

print("Student Grading System")

# Prompt user for input and convert to a float
score = float(input("Enter your score: "))

# Check the score range and assign a grade
if 100 >= score >= 90:  # A grade for scores between and including 90 and 100
    print("Your grade is A")
elif 89 >= score >= 80:  # B grade for scores between and including 80 and 89
    print("Your grade is B")
elif 79 >= score >= 70:  # C grade for scores between and including 70 and 79
    print("Your grade is C")
elif 69 >= score >= 60:  # D grade for scores between and including 60 and 69
    print("Your grade is D")
elif 60 >= score >= 0:   # F grade for scores below and including 60
    print("Your grade is F")
else:
    print("Invalid")     # Negative numbers or scores above 100

