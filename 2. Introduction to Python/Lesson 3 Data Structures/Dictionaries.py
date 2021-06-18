elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

print(elements["helium"])  # print the value mapped to "helium"

# insert "lithium" with a value of 3 into the dictionary
elements["lithium"] = 3

print("carbon" in elements)
print(elements.get("lithium"))
