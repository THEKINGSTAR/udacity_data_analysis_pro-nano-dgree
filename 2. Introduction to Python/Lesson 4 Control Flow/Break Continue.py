""" 
Break, Continue
Sometimes we need more control over when a loop should end, or skip an iteration.
 In these cases, we use the break and continue keywords, which can be used in both for and while loops.

break terminates a loop
continue skips one iteration of a loop
Watch the video and experiment with the examples below to see how these can be helpful.

Try It Out!
Below, you'll find two methods to solve the cargo loading program from the video. 
The first one is simply the one found in the video, which breaks from the loop when the weight reaches the limit. However, we found several problems with this. 
The second method addresses these issues by modifying the conditional statement and adding continue. 
Run the code below to see the results and feel free to experiment!

 """

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))
