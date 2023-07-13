"""
and 
or

Logical operators a.k.a. boolean operators, work off of True and False booleans values, hence the name.
"""

foo = 6

if foo >= 5 and foo <= 8:
    print(f'{foo} is between 5 and 8.')

"""
not

* note - `not` negates a condition - similar to ! in js
"""

bar = 2

if not (bar >= 5 and bar <= 8):
    print(f'{bar} is not within range.')
