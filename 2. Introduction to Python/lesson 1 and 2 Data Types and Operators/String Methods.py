print(len("this"))
print(type(12))
print("Hello world")

#"sample string": sample_string.lower()

my_string ="sebastian thrun"
print(my_string.islower())


print(my_string.count('a'))

print(my_string.find('a'))


"""One important string method: format()
We will be using the format() string method a good bit in our future work in Python, 
and you will find it very valuable in your coding, especially with your print statements.

We can best illustrate how to use format() by looking at some examples:
 """

#Example 1

print("Mohammed has {} balloons".format(27))

#Example 1 Output
#Mohammed has 27 balloons

##########################
#Example 2

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

#Example 2 Output
#Does your dog bite?

##########################
#Example 3

maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))

#Example 3 Output
#Maria loves math and statistics


##########################

""" 
Thanks for completing that!
That's right, an error occurs. 
The islower() method is an attribute of string methods, but not floats. 
Different types of object have methods specific to their type. 
For example, floats have the is_integer() method which strings don't have. """

#print(13.37.islower())

##########################

# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# and try them out here

name = "khaled mohamed fahllah mohamed"
print(name.capitalize())
print(name.casefold())

print(name.count("a"))
print(name.find("ll"))
print(name.isalpha())
print(name.upper())

##########################

# Write two lines of code below, each assigning a value to a variable
# Now write a print statement using .format() to print out a sentence and the
#   values of both of the variables

footbool_team_player = 11

status = "useualy the team would play with the main {} but to to enjery of hte main striker the team will play with main 9 plus 1"
print(status.format(footbool_team_player))
