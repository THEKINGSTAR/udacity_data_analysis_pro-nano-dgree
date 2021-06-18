""" 
Quiz: readable_timedelta
Write a function named readable_timedelta. 
The function should take one argument, an integer days, and return a string that says how many weeks and days that is.
For example, calling the function and printing the result like this:

print(readable_timedelta(10))

#should output the following:

1 week(s) and 3 day(s).
 """
# write your function here


def readable_timedelta(input_days):
    weeks = 0
    days = 0
    for i in range(input_days):
        if input_days >= 7:
            weeks += 1
            input_days = input_days - 7
        elif input_days < 7 and input_days > 0:
            days += 1
            input_days -= 1
    return("{} week(s) and {} day(s).".format(weeks, days))


# test your function
print(readable_timedelta(3769))

"""
readable_timedelta(1466)
The expected output is: 209 week(s) and 3 day(s).

readable_timedelta(7637)
The expected output is: 1091 week(s) and 0 day(s).

readable_timedelta(468)
The expected output is: 66 week(s) and 6 day(s).

readable_timedelta(1)
The expected output is: 0 week(s) and 1 day(s).

readable_timedelta(6)
The expected output is: 0 week(s) and 6 day(s).

readable_timedelta(7)
The expected output is: 1 week(s) and 0 day(s).

readable_timedelta(9)
The expected output is: 1 week(s) and 2 day(s).

readable_timedelta(3769)
The expected output is: 538 week(s) and 3 day(s)
"""

###############################################
""" 
Quiz Solution: readable_timedelta

 """
def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)


# test your function
print(readable_timedelta(10))
