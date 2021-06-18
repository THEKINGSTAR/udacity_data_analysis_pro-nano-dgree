points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names

points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names

if points <= 50:
    prize = "wooden rabbit"
elif points >= 51 and points <= 150:
    prize = None
elif points >= 151 and points <= 180:
    prize = "wafer-thin mint"
elif points >= 181 and points <= 200:
    prize = "penguin"

# use the truth value of prize to assign result to the correct prize

if prize == None:
    result = "Oh dear, no prize this time."
else:
    result = "Congratulations! You won a {}!".format(prize)

print(result)


########################################################################

""" points = 174

points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time." """
