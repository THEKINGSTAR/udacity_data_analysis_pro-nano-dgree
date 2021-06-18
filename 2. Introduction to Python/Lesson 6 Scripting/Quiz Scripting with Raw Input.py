# get and process input for a list of names
names = input("Please names seperated by comma :")
names_lst = names.split(",")


# get and process input for a list of the number of assignments
assignments = input("Please grade seperated by comma :")
assignments_lst = assignments.split(",")

# get and process input for a list of grades
grades =input("Please grade seperated by comma :")
grades_lst = grades.split(",")




# message string to be used for each student
# HINT: use .format() with this string in your for loop

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"


print(names_lst)
# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for n,a,g in zip(names_lst, assignments_lst, grades_lst):
    print(message.format(n, a, g, (int(g)+int(a)*2)))




#################################################################
""" 
Quiz Solution: Generate Messages
Here's one way you can implement this program! 
"""

names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
