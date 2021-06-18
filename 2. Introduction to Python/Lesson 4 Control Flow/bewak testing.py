manifest = [("bananas", 15), ("mattresses", 24),
            ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]


wihgt = 0
items_list = []

for cargo in manifest:
    if wihgt >= 100:
        break
    elif wihgt + cargo[1] > 100:
        break
    elif wihgt + cargo[1] <= 100:
        items_list.append(cargo[0])
        wihgt += cargo[1]
        mesage = "the items in the list is : {}, with wight of {}".format(
            cargo[0], cargo[1])
        print(mesage)


print(items_list)
print(wihgt)
