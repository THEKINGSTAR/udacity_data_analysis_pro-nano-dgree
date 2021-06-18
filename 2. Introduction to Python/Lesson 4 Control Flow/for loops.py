cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")

########################
###  VS  ###
########################
for i in "cities":
    print(i)
print("Done!")
########################
for i in range(3):
    print("Hello!")

################################################
#######   range(start=0, stop, step=1)   #######
################################################

print(list(range(4)))

print(list(range(2 , 6)))

print(list(range(3 , 10 , 2)))

###################################
#Modifying a list is a bit more involved,
#and requires the use of the range() function.
for index in range(len(cities)) :
    cities[index] = cities[index].title()

print(cities)

##################################
# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

print(capitalized_cities)
