""" 
If you already have programming experience, feel free to skip any exercises that you don't feel are necessary for you.

Practice: Factorials with While Loops
Find the factorial of a number using a while loop.

A factorial of a whole number is that number multiplied by every whole number between itself and 1. 
For example, 6 factorial (written "6!") equals 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.

We can write a while loop to take any given number and figure out what its factorial is.

Example: If number is 6, your code should compute and print the product, 720.
 """
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while  current <=6 :
    product= product * current
    #print("product : "+str(product))

    current +=1
    #print("current : "+str(current))
    

# multiply the product so far by the current number

# increment current with each iteration until it reaches number


# print the factorial of number
print(product)
##################################################################################################
""" 

# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)
 """
