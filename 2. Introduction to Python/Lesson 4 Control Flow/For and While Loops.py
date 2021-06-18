num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
indexing =0
add_up=0
first_five_odd=0
counter_odd=0
for indexing in range(len(num_list)):
    od_or_not = num_list[indexing] % 2
    #print("od_or_not "+str(od_or_not))
    if od_or_not > 0 and counter_odd < 5:
        add_up += num_list[indexing]
        counter_odd += 1
        first_five_odd += 1
indexing += 1
    
print(add_up)

##############################################################################
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list):
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print("The numbers of odd numbers added are: {}".format(count_odd))
print("The sum of the odd numbers added is: {}".format(list_sum))
