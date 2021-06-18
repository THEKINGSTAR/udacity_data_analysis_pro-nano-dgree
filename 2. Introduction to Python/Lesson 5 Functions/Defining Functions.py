""" Defining Functions
Example of a function definition:
 """


def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


print(cylinder_volume(10, 3))

# this prints something, but does not return anything


def show_plus_ten(num):
    print(num + 10)

# this returns something


def add_ten(num):
    return(num + 10)


print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))
###########################################################
""" Default Arguments
We can add default arguments in a function to have default values for parameters that are unspecified in a function call.

 """
def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2

""" 
In the example above, radius is set to 5 if that parameter is omitted in a function call. 
If we call cylinder_volume(10), the function will use 10 as the height and 5 as the radius. 
However, if we call cylinder_volume(10, 7) the 7 will simply overwrite the default value of 5.

Also notice here we are passing values to our arguments by position.
 It is possible to pass values in two ways - by position and by name. 
 Each of these function calls are evaluated the same way.
 """
print(cylinder_volume(10, 7))  # pass in arguments by position
print(cylinder_volume(height=10, radius=7))  # pass in arguments by name
