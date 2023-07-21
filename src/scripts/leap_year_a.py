
# leap year algo

# 1.) If the year is divisible by 4, it is a leap year.
# 2.) However, if the year is divisible by 100, it is not a leap year, unless...
# 3.) The year is divisible by 400, the year IS a leap year. Otherwise, it is NOT a leap year.

# Something like: year % 4 and (not year % 100 and year % 400)


# leap year program

# Program 1.) determine if a year is a leap year.
# Program 2.) takes a year and returns the FOLLOWING leap year, for instance, 2003 -> 2004.

def leap_year_validator(year: int) -> bool:
    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0

    if divisible_by_4 and (not divisible_by_100 or divisible_by_400):
        return True
    else:
        return False
    

# Program 1.) determine if a year is a leap year.

while True:
    year = int(input('Year:'))

    is_leap_year = leap_year_validator(year)

    if is_leap_year:
        print('Leap year.')
        break
    else:
        print('Not a leap year.')
