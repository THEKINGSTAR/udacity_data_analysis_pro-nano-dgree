""" A tuple is another useful container. 
It's a data type for immutable ordered sequences of elements. 
They are often used to store related pieces of information. 
Consider this example involving latitude and longitude: """

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

""" 
Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indices.
Unlike lists, however, tuples are immutable - you can't add and remove items from tuples, or sort them in place.

Tuples can also be used to assign multiple variables in a compact way. """

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))


tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])
