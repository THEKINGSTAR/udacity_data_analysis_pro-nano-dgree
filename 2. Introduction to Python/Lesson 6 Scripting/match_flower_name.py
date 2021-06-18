""" 
Practice Question
For the following practice question you will need to write code in Python in the workspace below. 
This will allow you to practice the concepts discussed in the Scripting lesson, such as reading and writing files.
 You will see some older concepts too, but again, we have them there to review and reinforce your understanding of those concepts.

Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. 
The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. 
It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

Sample Output:

>>> Enter your First [space] Last name only: Bill Newman
>>> Unique flower name with the first letter: Bellflower
Using this workspace

We have provided a programming environment with a Terminal and code editor, so you can do all your work right here. 
Here are a few tips orienting you to this kind of workspace.

On the top panel is a code editor where you can edit the Python file match_lower_name.py.
 Scroll up and down in this panel to see all the code. 
 You can also expand or shrink this panel by clicking and dragging its bottom border.
  We have included the flower.txt file that includes the list of unique flower names for each alphabet. 
  You can click on it in the left to open it in a new tab.

On the bottom panel, you can execute your Python file by clicking on New Terminal and entering python match_flower_name.py on the command line.

 """
# Write your code here
import os

file_location = os.getcwd()
filename = "flowers.txt"
# HINT: create a dictionary from flowers.txt
flowers_dictionary={}


def create_dictionary ():
    with open(file_location + "\\" + filename, "r") as oppend_file:
        file_data = oppend_file.read()
        for line in file_data.splitlines():
            temp_list = []
            temp_list = line.split(":")
            #print(temp_list)
            flowers_dictionary[temp_list[0]] = [temp_list[1]]


#print(flowers_dictionary)
###########################################################################
""" 
The main (separate) function should take user input (user's first name and last name) 
and parse the user input to identify the first letter of the first name. 
It should then use it to print the flower name with the same first letter
(from dictionary created in the first function).
 """
###########################################################################

# HINT: create a function to ask for user's first and last name


def separate(first):
    create_dictionary()
    name = str(first)
    if name.islower():
        name = name.upper()

    print("Unique flower name with the first letter: {}".format(
        flowers_dictionary[name[0]]))


first_name = input ("Enter your First [space] Last name only: ")

# print the desired output
separate(first_name.split(",")[0])

    
######################################################################################################################################

""" 
Quiz Solution:
Here's one way you can implement this program! 
"""

# function that creates a flower_dictionary from filename


def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower()
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

# Main function that prompts for user input, parses out the first letter
# includes function call for create_flowerdict to create dictionary


def main():
    flower_d = create_flowerdict('flowers.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
# print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(
        flower_d[first_letter]))


main()
