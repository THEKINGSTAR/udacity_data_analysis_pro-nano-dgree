#### Manipulating ndarrays

import numpy as np


# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
# Afterwards use Boolean indexing to pick out only the odd numbers in the array

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
X = np.arange(1, 26).reshape(5, 5)
#print(X)
# Use Boolean indexing to pick out only the odd numbers in the array
Y = X[X % 2 > 0]
#print(Y)





#############################################
## Solution
""" 
import numpy as np

X = np.arange(1,26).reshape(5,5)

Y = X[X % 2 != 0]
 """