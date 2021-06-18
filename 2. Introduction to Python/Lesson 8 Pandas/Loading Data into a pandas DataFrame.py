""" 
The GOOG.csv and fake_company.csv are available to download at the bottom of this page. If it doesn't get downloaded upon clicking, try right-click and choose the "Save As..." option.

In machine learning you will most likely use databases from many sources to train your learning algorithms. Pandas allows us to load databases of different formats into DataFrames. One of the most popular data formats used to store databases is csv. CSV stands for Comma Separated Values and offers a simple format to store data. We can load CSV files into Pandas DataFrames using the pd.read_csv() function. Let's load Google stock data into a Pandas DataFrame. The GOOG.csv file contains Google stock data from 8/19/2004 till 10/13/2017 taken from Yahoo Finance.
 """
import numpy as np
import pandas as pd
## Example 1. Load the data from a .csv file.
# We load Google stock data in a DataFrame
Google_stock = pd.read_csv('.\GOOG.csv')

# We print some information about Google_stock
print('Google_stock is of type:', type(Google_stock))
print('Google_stock has shape:', Google_stock.shape)


""" 
Google_stock is of type: class 'pandas.core.frame.DataFrame'
Google_stock has shape: (3313, 7)
"""

""" 
 We see that we have loaded the GOOG.csv file into a Pandas DataFrame and it consists of 3,313 rows and 7 columns. Now let's look at the stock data
"""
