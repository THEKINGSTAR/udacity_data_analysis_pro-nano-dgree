""" 
Quiz: Lambda with Map
map() is a higher-order built-in function that takes a function and iterable as inputs, 
and returns an iterator that applies the function to each element of the iterable. 
The code below uses map() to find the mean of each list in numbers to create the list averages. Give it a test run to see what happens.

Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map().

 """
numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]


def mean(num_list):
    return sum(num_list) / len(num_list)

mean=lambda num_list:sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)
#############################################################

""" 
#Quiz Solution: Lambda with Map
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)
 """
