#!/usr/bin/python3
age = float(input('Type in your age in order to know which year you were born: '))
year_of_birth = (2020 - age)
print("Your year of birth is", year_of_birth)

year_of_birth = int(input('Tell me when you were born and I will tell you how old you are: '))
how_old = 2020 - year_of_birth
if      year_of_birth <= 2020:
        print("You are", how_old, "years old.")
else:
        print("Your year of birth cannot go past the current year of 2020.")

    
    
