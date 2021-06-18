""" 
Variable Scope
Variable scope refers to which parts of a program a variable can be referenced, or used, from.

It's important to consider scope when using variables in functions. If a variable is created inside a
 """
# This will result in an error


def some_function():
    word = "hello"


print(word)


""" 
In the example above and the example below, word is said to have scope that is only local to each function.
 This means you can use the same name for different variables that are used in different functions.
 """


# This works fine
def some_function():
    word = "hello"


def another_function():
    word = "goodbye"



""" 
Variables defined outside functions, as in the example below, 
can still be accessed within a function. Here, word is said to have a global scope.
"""
# This works fine
word = "hello"


def some_function():
    print(word)


some_function()


""" 
otice that we can still access the value of the global variable word within this function. 
However, the value of a global variable can not be modified inside the function. 
If you want to modify that variable's value inside this function, it should be passed in as an argument. You'll see more on this in the next quiz.

Scope is essential to understanding how information is passed throughout programs in Python and really any programming language.

More on Variable Scope
When you program, you'll often find that similar ideas come up again and again. 
You'll use variables for things like counting, iterating and accumulating values to return.
 In order to write readable code, you'll find yourself wanting to use similar names for similar ideas. 
 As soon as you put multiple piece of code together
  (for instance, multiple functions or function calls in a single script) you might find that you want to use the same name for two separate concepts.

Fortunately, you don't need to come up with new names endlessly. 
Reusing names for objects is OK as long as you keep them in separate scope.

Good practice: It is best to define variables in the smallest scope they will be needed in. 
While functions can refer to variables defined in a larger scope, 
this is very rarely a good idea since you may not know what variables you have defined if your program has a lot of variables.

 """
