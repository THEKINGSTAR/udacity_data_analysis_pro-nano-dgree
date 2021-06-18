elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
            "helium": {"number": 2,
                       "weight": 4.002602,
                       "symbol": "He"}}


helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight


# create a new oxygen dictionary
oxygen = {"number": 8, "weight": 15.999, "symbol": "O"}
# assign 'oxygen' as a key to the elements dictionary
elements["oxygen"] = oxygen
print('elements = ', elements)
print(elements.get("helium"))


""" 
Quiz: Adding Values to Nested Dictionaries
Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary.
 After inserting the new entries you should be able to perform these lookups:
 """


elements['hydrogen']['is_noble_gas'] = True
elements['helium']['is_noble_gas'] = False

""" Your code passes all of our tests, nice work!
This is how I added values to the `elements` dict. 
The syntax for adding elements to nested data structures is about the same as it is for reading from them.
```python
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
```
"""
print(elements['hydrogen']['is_noble_gas'])
#False
print(elements['helium']['is_noble_gas'])
#True

""" 
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
 """
print('elements = ', elements)
