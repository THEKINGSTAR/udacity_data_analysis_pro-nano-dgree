""" Quiz: Create Usernames
Write a for loop that iterates over the names list to create a usernames list. 
To create a username for each name, 
make everything lowercase and replace spaces with underscores.
 Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

should create the list:

usernames = ["joey_tribbiani", "monica_geller",
             "chandler_bing", "phoebe_buffay"]

HINT: Use the .replace() method to replace the spaces with underscores. Check out how to use this method in this Stack Overflow answer.
 """

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for user in range(len(names)):
    usernames.append(names[user].replace(" ", "_").lower())


print(usernames)

""" 
Quiz Solution: Create Usernames
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames) """
###########################################################

""" Quiz: Modify Usernames with Range
Write a for loop that uses range() to iterate over the positions in usernames to modify the list. 
Like you did in the previous quiz, 
change each name to be lowercase and replace spaces with underscores. After running your loop, this list
 """
usernames = ["Joey Tribbiani", "Monica Geller",
             "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)):
    usernames[index] = usernames[index].replace(" ", "_").lower()

print(usernames)

""" 
Quiz Solution: Modify Usernames with Range
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames) """
###########################################################
""" Quiz: Tag Counter
Write a for loop that iterates over a list of strings, tokens, 
and counts how many of them are XML tags.
 XML is a data language similar to HTML.
 You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">".
  Keep track of the number of tags using the variable count.

You can assume that the list of strings will not contain empty strings.
 """

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for i in range(len(tokens)):
    if tokens[i][0] == "<" and tokens[i][-1] == ">":
        count +=1

print(count)

""" 
Quiz Solution: Tag Counter
You can use string indexing to find out if each token begins and ends with angle brackets.

tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)
 """
###########################################################

""" Quiz: Create an HTML List
Quiz: Create an HTML List
Write some code, including a for loop, 
that iterates over a list of strings and creates a single string, 
html_str, which is an HTML list. 
For example, if the list is items = ['first string', 'second string'], printing html_str should output:
<ul>
<li>first string</li>
<li>second string</li>
</ul>
##########
That is, the string's first line should be the opening tag <ul>. 
Following that is one line per element in the source list, surrounded by <li> and </li> tags.
 The final line of the string should be the closing tag </ul>.
 """
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items :
    html_str += "<li>"+ item+"</li>"+"\n"

html_str += "</ul>"+"\n"
print(html_str)

""" Quiz Solution: Create an HTML List
items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str) """
