"""
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
""" 
def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input(
        "Please select city name : ( chicago , new york city , washington)".title())
    city.lower()
    print("you chosed the city of  : {}".format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(
        "Please select filter type , all or monte , if month enter the name of the month (january, february, ... , june)")
    month.lower()
    print("you chosed to filter by : {}".format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please select filter type for day of week , all or day , if day enter the name of the day (all, monday, tuesday, ... sunday)")
    day.title()
    print("you chosed to filter by : {}".format(day))

    print('-'*40)

    #print(city, month, day)

    return city, month, day


get_filters()
 """

city = ''
while True:
    cites= ["chicago", "new york city", "washington" ]
    if city in cites:
       break
    else :
        city =input("Please select city name : ( chicago , new york city , washington)".title()).lower()

