
# Causing a Traceback

def a():
    print('Start of a()')
    b() # call b()

def b():
    print('Start of b()')
    c() # call c()

def c():
    print('Start of c()')
    42 / 0 # this will throw a zero division error

a() # invoke thy functions

"""
Examining the Error:

Start of a()
Start of b()
Start of c()
Traceback (most recent call last):
  File "/Users/zakmayfield/Dev/python/pythonforfun/src/scripts/traceback.py", line 16, in <module>
    a() # invoke thy functions
    ^^^
  File "/Users/zakmayfield/Dev/python/pythonforfun/src/scripts/traceback.py", line 6, in a
    b() # call b()
    ^^^
  File "/Users/zakmayfield/Dev/python/pythonforfun/src/scripts/traceback.py", line 10, in b
    c() # call c()
    ^^^
  File "/Users/zakmayfield/Dev/python/pythonforfun/src/scripts/traceback.py", line 14, in c
    42 / 0 # this will throw a zero division error
    ~~~^~~
ZeroDivisionError: division by zero


Breaking it Down:

- "Traceback (most recent call last):" indicates a traceback, and specifies the order. In this case the first call we do is `a()`
- The next line shows the tracebacks first function call, in this case the first call is still a(), on line 16.
- The line group under "Traceback (most..." is called the 'frame summary', they show the information inside a frame object. Frame objects store local variables and other data associated with the function call. Notice the difference in descrition between an error occuring in the global scope of the module vs within the scope of a function.
- 
"""