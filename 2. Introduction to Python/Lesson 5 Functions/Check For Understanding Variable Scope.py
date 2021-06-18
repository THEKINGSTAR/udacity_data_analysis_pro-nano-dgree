
##########################################################################
egg_count = buy_eggs(egg_count)
print(egg_count)

str1 = 'Functions are important programming concepts.'

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()
""" 
Thanks for completing that!
Correct! When we call the function, 

we use str1 = 'Variable scope is an important concept.' 

which has a local variable scope.

 """
##########################################################################
""" QUESTION 2 OF 5
Now let's say we tweak the code a bit and comment out str1 = 'Variable scope is an important concept.'
 """
str1 = 'Functions are important programming concepts.'
def print_fn():
    #str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()
""" 
Thanks for completing that!
Correct! When we comment out #str1 = 'Variable scope is an important concept.' we are basically removing its local scope. 
However, since str1 = 'Functions are important programming concepts.' has global scope,
 when we call the function it will print it because of the global scope
 """
##########################################################################
""" 
QUESTION 3 OF 5
We made another tweak to the code.
 """
def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)


print_fn(str1)
""" 
Thanks for completing that!
That's right! The function definition did not have any arguments. So it will give us an error.
"""
##########################################################################
""" QUESTION 4 OF 5
We made a final tweak to the code.
 """
str1 = 'Functions are important programming concepts.'
def print_fn():
    print(str1)


print_fn(str1)

# Now what do you think will happen?
""" 
Thanks for completing that!
You got it! As long as the function definition did not include any arguments,
 the function call written as print_fn(str1) will give an error as it was not seeking an argument.

 """
