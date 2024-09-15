#WAP in python that will ask a year that you were born in and then calculate the age and print it on the terminal

# year_born = int(input("Enter the year you were born : "))
# curr_year = 2024
# curr_age = str(curr_year - year_born)

# print("Your age is " + curr_age)
# print(type(curr_age))

year_born = input("Enter the year you were born : ")
curr_year = 2024
curr_age = curr_year - int(year_born)

print(curr_age)
print(type(curr_age))
