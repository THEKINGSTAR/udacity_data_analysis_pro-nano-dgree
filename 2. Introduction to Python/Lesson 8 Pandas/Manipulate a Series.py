import pandas as pd

# DO NOT CHANGE THE VARIABLE NAMES

# Given a list representing a few planets
planets = ['Earth', 'Saturn', 'Venus', 'Mars', 'Jupiter']

# Given another list representing the the distance of the selected planets from the Sun
# The distance from the Sun is in units of 10^6 km
distance_from_sun = [149.6, 1433.5, 108.2, 227.9, 778.6]


# TO DO: Create a Pandas Series using the lists above, representing the distance of some planets from the Sun.
# Use the `distance_from_sun` as your data, and `planets` as your index.
dist_planets =pd.Series(planets,distance_from_sun)


# TO DO: Calculate the time (minutes) it takes sunlight to reach each planet.
# You can do this by dividing each planet's distance from the Sun by the speed of light.
# Use the speed of light, c = 18, since light travels 18 x 10^6 km/minute.
c = 18
time_light = dist_planets[planets]/c
time_light


# TO DO: Use Boolean indexing to select only those planets for which sunlight takes less
# than 40 minutes to reach them.
close_planets = time_light[time_light < 40]
close_planets

#############################################################################################################
####################            SOLUTION    #################################################################
#############################################################################################################

distance_from_sun = [149.6, 1433.5, 108.2, 227.9, 778.6]

planets = ['Earth', 'Saturn', 'Venus', 'Mars', 'Jupiter']

dist_planets = pd.Series(data= distance_from_sun, index = planets)

time_light = dist_planets / 18

close_planets = time_light[time_light < 40]
