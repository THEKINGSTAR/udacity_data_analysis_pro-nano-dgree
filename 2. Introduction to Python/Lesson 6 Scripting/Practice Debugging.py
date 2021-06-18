""" 

Quiz: Practice Debugging
In the workspace at the bottom of the page, there is a piece of code in the user_input_numlist.py Python file.
 The code prompts the user to enter 10 two-digit numbers. 
 It should then find and print the sum of all of the even numbers among those that were entered.

But there is a bug in the code! When I input a number, I get the following TypeError.
 Use the programming environment provided below with a Terminal and code editor to debug the code.

 """



""" 
Using the workspace:

Here are a few tips orienting you to this kind of workspace.

In the top panel is a code editor where you can edit the Python file user_input_numlist.py. 
Scroll up and down in this panel to see all the code. You can also expand or shrink this panel by clicking and dragging its bottom border.

In the bottom panel, you can execute your Python file by clicking on New Terminal and entering python user_input_numlist.py on the command line.

The solutions have been provided on the next page, but I encourage you to try figuring out where the bug is in the code, and fixing it yourself.

Sample Output: This is what the output should look like.

 """

# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers
for i in range(10):
    userInput = input("Enter any 2-digit number: ")

# check to see if number is even and if yes, add to list_sum
# print incorrect value warning  when ValueError exception occurs
    try:
        # number = int(userInput)
        number = userInput
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))


#########################################################################################################################

""" 
Solutions for Quiz: Practice Debugging
The code prompts the user for 10 two-digit numbers.
 It is supposed to then find and print the sum of all of the even numbers among those that were entered.
  But there is a bug in the code, because when I input a number, I get a TypeError.

How can I find the bug in the code and debug it?

I added a print statement to check the datatype of the variable holding the number input by the user. 
print(type(userInput)). I added this statement after the line userinput = input("Enter any number: ").
The output showed:
'class 'str' followed by TypeError: not all arguments converted during string formatting.
This meant that the variable userInput had a datatype of a string, but we need the datatype to be int instead. The datatype for userInput needed to be changed to int.
To fix the error, I used the built-in function int()to return an integer object from the value input by the user. See my solution below:
Here is my solution:
 """
user_list = []
list_sum = 0
for i in range(10):
    userInput = int(input("Enter any number: "))
    try:
        user_list.append(userInput)
        if userInput % 2 == 0:
            list_sum += userInput
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))
