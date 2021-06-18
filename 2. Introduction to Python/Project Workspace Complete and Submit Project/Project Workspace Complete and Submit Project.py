import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

#########################################################################################################################################################################################

############## TESTING ##############
""" 
df = pd.read_csv(CITY_DATA["chicago"])
df 
"""
#####################################

#########################################################################################################################################################################################


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while True:
        cites = ["chicago", "new york city", "washington"]
        if city in cites:
            break
        else:
            print(
                "city to select from [chicago, new york city, washington]".title())
            city = input(
                "Please select city name : ( chicago , new york city , washington)\n".title()).lower()
    print("you chosed the city of  : {}".format(city).title())
    #########################################################################################################
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if (month in months) or (month == 'all'):
            break
        else:
            print(
                "\nmonths to select from is : ['january', 'february', 'march', 'april', 'may', 'june'] ".title())
            month = input(
                "Please select filter type , 'all' or 'monte name' , if month enter the name of the month (january, february, ... , june)\n".title()).lower()
    print("you chosed to filter by : {}".format(month))
    #########################################################################################################
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while True:
        days = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]
        if (day in days) or (day == 'All'):
            break
        else:
            print("\nfilter by day  enter day name : ".title())
            day = input(
                "\nPlease select filter type for day of week , 'all' or day , if day enter the name of the day (all, monday, tuesday, ... sunday)\n").title()

    if day == "All":
        day = day.lower()
    print("you choses to filter by : {}".format(day).title())
    print("data will be showing for cit of '{}' in mont of '{}' in day of '{}'.".format(city,month,day).title())
    #########################################################################################################
    print('-'*40)

    #print( city, month, day)

    return city, month, day


############## TESTING ##############
### get_filters()
#####################################
""" 
Inputs not handled correctly

Data could not be loaded properly. Could you please change the input process so examples looking as follows are accepted?:
washington, january, monday
barcelona, WaSHINGTON, january, MonDAY (in this example, the first introduced city is rejected because it's not among the choosable ones)
washington, jUNe, mOnDAy
washington, March, Tuesday
washington, aLL, All

Please, notice how input handling must be case insensitive (both washington and WasHingTON should be accepted). 
As a suggestion, I would recommend you to transform the input written by the user using the 'lower' function. 
This transformation will allow you to accept as valid all the different inputs you should expect given the rubrics especifications: washington, Washington, WaSHINgton, WASHINGTON...

When reviewing these inputs, please make sure you don't only test get_filters, but also you pass the returned values to load_data. 
This way you'll be able to ensure the whole process works as expected.
"""
""" 
WaSHINGTON, january, MonDAY
washington, jUNe, mOnDAy
washington, March, Tuesday
washington, aLL, All
 """
###I FAILED TO FIND THE ERRORE   ALL TESTING VALUES PASSED THE TESTING (washington, Washington, WaSHINgton, WASHINGTON) :( 😒😒😒😎✌
#####################################

#########################################################################################################################################################################################


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    ## load data based on the arg() from caling the load_date function
    df = pd.read_csv(CITY_DATA[city])

    ## converting the start time string to date time to extract from
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month_name()
    # df['day']   = df['Start Time'].dt.day
    df['Day'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)

        # filter by month to create the new dataframe
        df = df[df['Start Time'].dt.month == month+1]

    # filter by day of week if applicable
    if day != 'all':
        # create filter of day
        ## using the day index in case we asked the user to enter number of the day in the week
        # days = ['Sunday', 'Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday']
        # day  = days.index(day)+1

        # filter by day of week to create the new dataframe
        df = df[df['Start Time'].dt.day_name() == day]

    return df
############## TESTING ############
## test_case
#load_data('chicago', 'april', 'Sunday')
#load_data('chicago', 'all', 'all')
###################################
## get help to extract day name
#df = df['Start Time'].dt.day_name()
## help link:(https://www.youtube.com/watch?v=6cjXwYqgreE)
## help link:(https://stackoverflow.com/questions/60339049/weekday-name-from-a-pandas-dataframe-date-object)

#df = df['Start Time'].dt.day_name()
#####################################

#########################################################################################################################################################################################


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]
    print('\nMost Frequent Month      :', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['Day'].mode()[0]
    print('\nMost Frequent day        :', popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('\nMost Frequent Start Hour :', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


############## TESTING ##############
""" df=load_data('chicago', 'all', 'all')
time_stats(df)
 """
#df
#####################################


#########################################################################################################################################################################################
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df["Start Station"].mode()[0]
    print('\nMost Commonly used start station :'.title(), commonly_start_station)

    # TO DO: display most commonly used end station
    commonly_end_station = df["End Station"].mode()[0]
    print('\nMost Commonly used end station   : {}'.format(
        commonly_end_station).title())

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end_station = (
        df["End Station"]+" "+df["Start Station"]).mode()[0]
    print('\nMost Frequent day of start station and end station trip               :',
          combination_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


############## TESTING ##############
""" df=load_data('washington', 'all', 'all')
station_stats(df) """
#####################################

#########################################################################################################################################################################################


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum().sum()
    print('\ntotal travel time   : {} hours'.format(total_travel_time).title())

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print('\nmean travel time    : {} hours'.format(mean_travel_time).title())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


############## TESTING ##############
""" df = load_data('chicago', 'april', 'Sunday')
trip_duration_stats(df) """
#####################################


#########################################################################################################################################################################################
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_users = df['User Type'].count()
    print('\nTotal number of users    : {} users'.format(count_users).title())
    # print value counts for each user type
    user_types = df["User Type"].value_counts()
    print(user_types)

    #####################################################################################################
    """ 
      Washington data does not have Gender and Birth Year columns. 
      When user selects Washington as the city your code throws an error. 
      You need to write some control points here. 
      If user choose Washington as city, then this control point should skip Gender and Birth Year analyses.
     """
    #####################################################################################################
    ################################   CHECKING FOR GENDER   ############################################
    # TO DO: Display counts of gender
    if 'Gender' in df:
        # Only access Gender column in this case
        count_gender = df['Gender'].count()
        print('\nTotal count gender of users    : {} users'.format(
            count_gender).title())

        gender = df["Gender"].value_counts()
        print(gender)

    else:
        print("\nGender stats cannot be calculated ,because 'Gender' does not appear in the dataframe")

    #####################################################################################################
    ################################   CHECKING FOR Birth Year  #########################################
    if 'Birth Year' in df:
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('\nearliest birth year    : {}'.format(
            earliest_birth_year).title())

        recent_birth_year = df['Birth Year'].max()
        print('\nrecent birth year      : {}'.format(recent_birth_year).title())

        most_birth_year = df['Birth Year'].mode()[0]
        print('\nmost birth year        : {}'.format(most_birth_year).title())
    else:
        print("\nBirth Year stats cannot be calculated ,because Birth Year does not appear in the dataframe")
    #####################################################################################################
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


############## TESTING ##############
""" 
df=load_data('Washington', 'april', 'Sunday')
user_stats(df)  
"""
#####################################

#########################################################################################################################################################################################
""" 
Descriptive statistics are correctly computed and used to answer the questions posed about the data. 
Raw data is displayed upon request by the user in this manner: Script should prompt the user if they want to see 5 lines of raw data, 
display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'.
"""
########  Missing functionality: #######
""" 
There is a missing functionality! The user must be able to ask you to show some rows of data upon request.

Please create a new function for this, for example called display_data. 
You need to ask the user whether he wants to see 5 rows of data. 
We will show all parts of analysis then we will ask this question: Do you want to see 5 rows of data.
 But it is not only the first 5 data but as much as the user wants. 
 For example, you asked the user like this in the first step: "Do you want to see the first 5 rows of data?". 
 He typed yes and you will show the first 5 rows ,then you ask again " Do you want to see the next 5 rows of data?" then he says yes and you show the next 5 data.
  You need to keep asking until he says no.
##############
## Here are some hints and template code:
we will show the data based on the location. 
namely, we will show the first 5 data in the first attempt, then second 5 data for the second "yes" So we need to keep track of this. How? (I used start_loc variable)
please check the iloc function. It returns dataframe based on the position. 
For example df.iloc[0:5] will return first 5 rows of data
what should be our condition for while condition? Remember, as long as the user does not enter no, we are inside in the loop.
Dont forget to ask the question inside the loop, otherwise it will be infinite loop.
"""
def viewing_data_frame(df):

    view_data = input("Would you like to view 5 rows of individual trip data? Enter 'yes' or 'no'?")
    start_loc = 5
    while view_data != 'no':
        print(df.iloc[0:start_loc].reset_index())
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


############## TESTING ##############
""" 
df=load_data('chicago', 'april', 'Sunday')
viewing_data_frame(df)  
"""
#####################################
## get help to understand how to select rows from the data frame :) 
## help link: // www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
#####################################

#########################################################################################################################################################################################
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        viewing_data_frame(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
