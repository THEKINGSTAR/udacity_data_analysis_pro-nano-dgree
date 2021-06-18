""" Quiz: len()
Use string concatenation and the len() function to find the length of a certain movie star's actual full name.
 Store that length in the name_length variable. 
Don't forget that there are spaces in between the different parts of a name! """

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

full_name = given_name + " " + middle_names + " " + family_name
name_length =len(full_name)  # todo: calculate how long this name is

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)



##Another solution
""" You calculated the correct value for name_length. Nice work!
I calculated my answer like this: """

name_length = len(given_name + middle_names + family_name) + 2 # The + 2 accounts for the spaces in between each word.
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

############################################################
#print(len(835))
""" Nice! The error message generated reads: TypeError: object of type 'int' has no len(), 
which alludes to the fact that len only works on a "sequence (such as a string, bytes, tuple, list, or range)
 or a collection (such as a dictionary, set, or frozen set)," as per the Python documentation. """


############################################################################################################################
""" Here are our solutions to some quizzes on the previous page:

Solution: Fix the Quote
Here are two different methods to fix the quote:

    # TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

# TODO: Fix this string!
ford_quote = "Whether you think you can, or you think you can't--you're right."
Solution: Write a Server Log Message
Here are a couple of options for this one:

print(username + " accessed the site " + url + " at " + timestamp + ".")
OR

message = username + " accessed the site " + url + " at " + timestamp + "."
print(message)
Solution: len()
name_length = len(given_name) + len(middle_names) + len(family_name) + 2
 """

