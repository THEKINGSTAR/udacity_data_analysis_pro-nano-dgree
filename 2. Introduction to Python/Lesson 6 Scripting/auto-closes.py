##############################################################################################################################################
""" 
With
Python provides a special syntax that auto-closes a file for you once you're finished using it. 
"""
import os

file_location = os.getcwd()

with open(file_location + "\\"+"test.txt") as f:
    file_data = f.read()
    print(file_data)

""" This with keyword allows you to open a file, do operations on it,
 and automatically close it after the indented code is executed, 
in this case, reading from the file. 
Now, we don’t have to call f.close()! You can only access the file object, f, within this indented block.
 """
