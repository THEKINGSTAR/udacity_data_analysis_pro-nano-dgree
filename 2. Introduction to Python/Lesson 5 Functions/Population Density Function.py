""" 
Quiz: Population Density Function
Write a function named population_density that takes two arguments, 
population and land_area, and returns a population density calculated from those values. 
I've included two test cases that you can use to verify that your function works correctly.
Once you've written your function, use the Test Run button to test your code.
# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

 """

# write your function here


def population_density(population , land_area):
    return(population/land_area)

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))
