""" 
Syntax of Python open file function

file_object  = open("filename", "mode") 

 """

import os

file_location = os.getcwd()
print(file_location)


opened_file = open(file_location +"\\"+"test.txt")
file_data = opened_file.read()

print(file_data)

opened_file.close()

#######################################################################################################
#####################################     Writing To Files       ######################################
#######################################################################################################

""" 
import os
file_location = os.getcwd()
print(file_location)

oppend_file= open(file_location+ "\\" +"test.txt", "a+" )

file_data=oppend_file.read()

print(file_data)

for i in range (1,8):
    oppend_file.write("Writing frompython editor %d\r\n"%i)
    
print(file_data)

oppend_file.close()

 """

#######################################################################################################
#####################################     Writing To Files       ######################################
#######################################################################################################

""" 
Open the file in writing ('w') mode. If the file does not exist, Python will create it for you. 

If you open an existing file in writing mode, any content that it had contained previously will be deleted. 
If you're interested in adding to an existing file, without deleting its content, you should use the append ('a') mode instead of write.
Use the write method to add text to the file.
Close the file when finished.

 """
f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()
