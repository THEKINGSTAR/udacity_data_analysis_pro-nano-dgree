import numpy as np

# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third
# column full of 3s, etc..

# Do not change the name of this array.
# Please don't print anything from your code! The TEST RUN button below will print your array.
###### X =

#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
###############     SOLUTION        #########################################################################################
# We will make use of array multiplication, as demonstrated on the previous page:
# "Example 6. Arithmetic operations on 2-D arrays (Compatible shape)"


# np.ones((4,4)) will give you a 4 x 4 matrix
#[[1. 1. 1. 1.],
# [1. 1. 1. 1.],
# [1. 1. 1. 1.],
# [1. 1. 1. 1.]]

# np.arange(1,5) will give you a 1 x 4 matrix
# [1 2 3 4]

# X can be calculated by multiplying the above two matrices, as shown below, to get:
#[[1. 2. 3. 4.],
# [1. 2. 3. 4.],
# [1. 2. 3. 4.],
# [1. 2. 3. 4.]]
X = np.ones((4, 4)) * np.arange(1, 5)
print(X)