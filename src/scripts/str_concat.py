# String concatenating

# Storytime program

# Program should prompt use for words, one at a time.
# Program should end if the user types the word 'end'
# Program should print a string containing all of the words inputted by the user

"""
Example:

Please type in a word: Once
Please type in a word: upon
Please type in a word: a
Please type in a word: time
Please type in a word: there
Please type in a word: was
Please type in a word: a
Please type in a word: girl
Please type in a word: end
Once upon a time there was a girl
"""

story = ""

while True:
    word = input("Please type in a word:")

    if len(story) > 0:
      last_word = story.split()[-1]
      if word == 'end' or word == last_word:
          break
      
    if word == 'end':
       break
    
    story += f"{word} "


print(story.strip())