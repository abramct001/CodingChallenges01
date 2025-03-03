#-----------------------------------------------------------------------------
# Name:        Temperature Advice (temp_code.py)
# Purpose:     Provides clothing recommendations based on temperature
#
# Author:      TA - 1034286
# Created:     26-Feb-2025
#-----------------------------------------------------------------------------

print("Temperature Advice")

# Prompt user to enter temperature and convert input to an integer
temperature = int(input("Enter your temperature: "))

# Check temperature range and give appropriate advice
if 10 >= temperature >= -50:  # If temperature is between -50 and 10, it's cold
    print("It's cold outside. Wear a jacket!")
elif 25 >= temperature >= 10:  # If temperature is between 10 and 25, it's mild
    print("It's a nice day. Wear short-sleeves.")
elif 25 <= temperature <= 50:  # If temperature is between 25 and 50, it's hot
    print("It's hot outside. Stay cool!")
else:
    print("Invalid")           # Invalid temperature values outside the -50 to 50 range