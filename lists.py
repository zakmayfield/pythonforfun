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