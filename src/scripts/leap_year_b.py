
# # Program 2.) takes a year and returns the FOLLOWING leap year, for instance, 2003 -> 2004.
def leap_year_validator(year: int) -> bool:
    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0

    if divisible_by_4 and (not divisible_by_100 or divisible_by_400):
        return True
    else:
        return False

year = int(input('Year:'))
next_year = year + 1

while not leap_year_validator(next_year):
    next_year += 1

print(f"The next leap year after {year} is {next_year}")