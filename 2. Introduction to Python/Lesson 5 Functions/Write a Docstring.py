""" 

Quiz: Write a Docstring
Write a docstring for the readable_timedelta function you defined earlier!
 Remember the way you write your docstrings is pretty flexible!
  Look through Python's docstring conventions here and check out this Stack Overflow page for some inspiration!
 """


def readable_timedelta(days):
    # insert your docstring here
    """IN THIS FUNCTION ONE INPUT IN TOW OUTPUT OUT
    @param param1: >>> INPUT IS NUMBER OF DYAS 
    OUTPUT IS WEEKS AND DAY EQUAL TO SUM OF THE INPUTED DAYS !!!
    FEEL STUPID ABOUT IT ?? WRITE YOUR OWN FUNCTION !!!!
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
##############################################################################################
##############################################################################################
##############################################################################################
""" 
Quiz Solution: readable_timedelta
Here's some ways you could've written your docstring!
 """


def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days."""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

##############################################################################################
def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days.

    Args:
        days (int): number of days to convert
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

##############################################################################################
def readable_timedelta(days):
    """
    Return a string of the number of weeks and days included in days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
