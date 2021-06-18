""" 
Practice: Factorials with For Loops
Now use a for loop to find the factorial!

It will now be great practice for you to try to revise the code you wrote above to find the factorial of a number, 
but this time, using a for loop. Try it in the code editor below!
 """
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1
# write your for loop here
for multi in range(2,number+1) :
    product=product*multi
    #print(product)
# print the factorial of number
print(product)


###################################################################################
""" 
Solution: Factorials with For Loops
Here is our solution for this one, using a for loop to find the factorial of a number:


# number we'll find the factorial of
number = 6
# start with our product equal to one
product = 1

# calculate factorial of number with a for loop
for num in range(2, number + 1):
    product *= num

# print the factorial of number
print(product)

 """
