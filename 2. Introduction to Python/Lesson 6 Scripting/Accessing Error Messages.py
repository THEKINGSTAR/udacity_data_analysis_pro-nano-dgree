""" Accessing Error Messages
When you handle an exception, you can still access its error message like this: """

try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))

""" This would print something like this:

ZeroDivisionError occurred: integer division or modulo by zero
So you can still access error messages, even if you handle them to keep your program from crashing!

If you don't have a specific error you're handling, you can still access the message like this: """

try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))

""" Exception is just the base class for all built-in exceptions. You can learn more about Python's exceptions """
""" 
https://docs.python.org/3/library/exceptions.html#bltin-exceptions
 """
