""" Techniques for Importing Modules
There are other variants of import statements that are useful in different situations.
 """
# To import an individual function or class from a module:
from module_name import object_name

# To import multiple individual objects from a module:
from module_name import first_object, second_object

# To rename a module:
import module_name as new_name

# To import an object from a module and rename it:
from module_name import object_name as new_name

# To import every object individually from a module (DO NOT DO THIS):
from module_name import *

# If you really want to use all of the objects from a module, 
# use the standard import module_name statement instead and access each of the objects with the dot notation.
import module_name


""" 

Modules, Packages, and Names
In order to manage the code better, modules in the Python Standard Library are split down into sub-modules that are contained within a package.
 A package is simply a module that contains sub-modules. A sub-module is specified with the usual dot notation.

Modules that are submodules are specified by the package name and then the submodule name separated by a dot. You can import the submodule like this.

 """


import package_name.submodule_name