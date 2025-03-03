#-----------------------------------------------------------------------------
# Name:        Day of the Week Activity Recommender (day_code.py)
# Purpose:     Suggests an activity based on the entered day
#
# Author:      TA - 1034286
# Created:     26-Feb-2025
#-----------------------------------------------------------------------------

print("Day of the Week Activity Recommender")
# Prompt user to enter a day and store as a string
day = input("Enter the day of the week: ")

# Convert input to lowercase to avoid case-sensitivity
day = day.lower()

# Check the entered day and recommend an activity
if day == "monday":
    print("Start your week with a workout")
elif day == "tuesday":
    print("It's a great day to read a book!")
elif day == "wednesday":
    print("Mid-week movie night!")
elif day == "thursday":
    print("Try a new recipe")
elif day == "friday":
    print("Relax and enjoy the weekend")
elif day == "saturday":
    print("Go for a hike")
elif day == "sunday":
    print("Prepare for the week ahead with some self-care")
else:
    print("Invalid")