# Program to read day,month,year. Then display the corresponding date in the format DD/MM/YYYY. Also check whether the year is a leap year or not
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if is_leap_year(year):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")

print(f"The entered date is: {day:02}/{month:02}/{year}")
