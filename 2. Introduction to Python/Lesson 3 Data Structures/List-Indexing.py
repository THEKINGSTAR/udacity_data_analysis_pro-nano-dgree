""" Quiz: List Indexing
Use list indexing to determine how many days are in a particular month based on the integer variable month,
 and store that value in the integer variable num_days. 
 For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.

Remember to account for zero-based indexing! """




month = 8
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# use list indexing to determine the number of days in month
num_days=days_in_month[8-1]

print(num_days)

##########################################################################

""" Quiz: Slicing Lists
Select the three most recent dates from this list using list slicing notation. 
Hint: negative indexes work in slices! """

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']


# TODO: Modify this line so it prints the last three elements of the list

print(eclipse_dates[-3:])

##########################################################################

""" QUESTION 3 OF 3
Suppose we have the following two expressions, sentence1 and sentence2:
 """
sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]


sentence2[6]="!"
print(sentence2)

sentence2[0]="Our Majesty"
print(sentence2)

##Errore message
#print(sentence1[30]="!")

sentence2[0:2] = ["We", "want"]
print(sentence2)
""" 
Thanks for completing that!
Here's our answer:

sentence1 is a string, and is therefore an immutable object. 
That means that while you can refer to individual characters in sentence1(e.g., you can write things like sentence1[5])
 you cannot assign value to them(you cannot write things like sentence1[5]='a').
  Therefore the third expression will result in an error.

sentence2 is a list, and lists are mutable, meaning that you can change the value of individual items in sentence2:

In the first expression we changed the value of the last item in sentence2 from "." to "!".
In the second expression we changed the value of the first item in sentence2 from "I" to "Our Majesty".
In the last expression we used slicing to simultaneously change the value of both the first and the second item in sentence2 from "I" and "wish" to "We" and "want".
 """

VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX', 'BAC', 'JNJ', 'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']

print(VINIX[0])
#>> > C
print(VINIX[1])
#>> > MA


print('GE' in VINIX)
#>> > False

print('GOOGL' in VINIX)
#>> > True


name="jim"
student=name
print(student)

name="tim"

print(student)
