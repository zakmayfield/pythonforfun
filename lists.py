"""
Lists - mutable - store collections of data with []
Tuple - immutable - store collections of data with ()
"""

"""
Multiple assignment -- relatable to destructuring in js
"""

fruits = ['apple', 'banana', 'starfruit']

apple, banana, starfruit = fruits

print(apple, banana, starfruit) # 'apple' 'banana' 'starfruit'

"""
index()
"""
print(fruits.index('banana')) # 1

"""
append()
"""
fruits.append('kiwi')
print(fruits) # ['apple', 'banana', 'starfruit', 'kiwi']

"""
del() - by index
remove() - by value

* note - when using remove(), if duplicate values, only the first instance will be removed
"""
del fruits[0]
fruits.remove('banana')
print(fruits) # ['starfruit', 'kiwi']

"""
sort()
sorted() - built in

* note - you can pass kwargs to sort(), such as reverse=True
"""

letters = ['z', 'a', 'b']

letters.sort()
print(letters) # ['a', 'b', 'z']

letters.sort(reverse=True)
print(letters) # ['z', 'b', 'a']

newly_sorted = sorted(letters)
print(newly_sorted) # ['a', 'b', 'z']