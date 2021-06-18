# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai': 17.8, 'Istanbul':13.3,'Karachi':13.0, 'Mumbai':12.5}


print(population)
print(population.get('dilithium'))


#None
print(population['Istanbul'])
##########population['dilithium']
#KeyError: 'dilithium'
print(population.get('kryptonite', 'There\'s no such element!'))
#"There's no such element!"


# Test the code here if you'd like
a = [1, 2, 3]
b = a
c = [1, 2, 3]


print(a == b)
print(a is b)
print(a == c)
print(a is c)


population = {'Shanghai': 17.8,
              'Istanbul': 13.3,
              'Karachi': 13.0,
              'Mumbai': 12.5}

population = {'Shanghai': 17.8, 'Istanbul': 13.3,'Karachi': 13.0, 'Mumbai': 12.5}
