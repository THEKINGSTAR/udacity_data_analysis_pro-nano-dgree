""" Quiz: String Methods Coding Practice
Below, we have a string variable that contains the first verse of the poem, If by Rudyard Kipling.
 Remember, is a special sequence of characters that causes a line break (a new line).

verse = "If you can keep your head when all about you Are losing theirs and blaming it on you,
If you can trust yourself when all men doubt you,
  But make allowance for their doubting too;
  If you can wait and not be tired by waiting,
 Or being lied about, don’t deal in lies,
 Or being hated, don’t give way to hating,
   And yet don’t look too good, nor talk too wise:"
Use the code editor below to answer the following questions about verse and use Test Run to check your output in the quiz at the bottom of this page.

What is the length of the string variable verse?
What is the index of the first occurrence of the word 'and' in verse?
What is the index of the last occurrence of the word 'you' in verse?
What is the count of occurrences of the word 'you' in the verse?
You will need to refer to Python's string methods documentation.
 """


verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)
print(len(verse))
print(verse.find("and"))
print(verse.rfind("you")) #reverse find find from the last of the string
print(verse.count("you"))

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!


##################################################################################################
""" 
Solution: String Methods Practice
Version 1 """

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

print("Verse has a length of {} characters.".format(len(verse)))
print("The first occurence of the word 'and' occurs at the {}th index.".format(
    verse.find('and')))
print("The last occurence of the word 'you' occurs at the {}th index.".format(
    verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))

""" Version 2
Here's another way you could write the print statements and get the same output. """

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."

length = len(verse)
first_idx = verse.find('and')
last_idx = verse.rfind('you')
count = verse.count('you')

print(message.format(length, first_idx, last_idx, count))
