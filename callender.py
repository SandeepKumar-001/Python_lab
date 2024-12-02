#write a program to check whether a given year is  a leap year or not.#?

def is_leap_year(year):
    # A year is a leap year if:
    # 1. It is divisible by 4
    # 2. If it is divisible by 100, it must also be divisible by 400

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")