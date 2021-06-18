""" QUIZ QUESTION
Read through this code snippet:
 """
egg_count = 0
def buy_eggs():
    egg_count += 12  # purchase a dozen eggs

buy_eggs()

#What is the result of running this code? If you aren't sure, try running it on your own computer!


""" 
This causes an UnboundLocalError, since Python doesn't allow functions to modify variables that are outside the function's scope.
 A better way would be to pass the variable as an argument and reassign it outside the function. See more on this in the next page.
 """

##########################################################################
################# THIS WILL WORK FINE ####################################
##########################################################################
egg_count = 0


def buy_eggs(egg_count):
    egg_count += 12  # purchase a dozen eggs
    return egg_count


print(buy_eggs(egg_count))
##########################################################################

egg_count = 0


def buy_eggs(count):
    return count + 12  # purchase a dozen eggs
