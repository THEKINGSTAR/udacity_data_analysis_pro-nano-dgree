""" When to use Dictionaries?
Let's revisit our Wall Street example from before. 
Previously we created a list for the index fund, 
Vanguard Institutional Index Fund,
 because we wanted to print the names of the holdings ( or stocks) in the index fund.

Now, let's say as the investment fund manager for VINIX, 
you also want to print a few more details for each holding. For e.g., what is your rate of return on each of the holdings?

A dictionary will work well here as there is a key: value association.
In other words, there is a linkage between each holding and the information(e.g., rate of return), 
and it can be organized under one index fund, VINIX. """

""" VINIX = {'C': 0.74, 'MA': 0.78, 'BA': 0.79, 'PG': 0.85, 'CSCO': 0.88, 'VZ': 0.9, 'PFE': 0.92, 'HD': 0.97, 'INTC': 1.0, 'T': 1.01, 'V': 1.02, 'UNH': 1.02, 'WFC': 1.05,
         'CVX': 1.05, 'BAC': 1.15, 'JNJ': 1.41, 'GOOGL': 1.46, 'GOOG': 1.47, 'BRK.B': 1.5, 'XOM': 1.52, 'JPM': 1.53, 'FB': 2.02, 'AMZN': 2.96, 'MSFT': 3.28, 'AAPL': 3.94} """

""" You can add even other details, such as rate of return YTD. For that we can add the details into the value associated with the key, i.e., the ticker symbol for the holding.
Like this: """

VINIX = {   'C': [0.74, -6.51],  'MA': [0.78, 34.77],  
            'BA': [0.79, 17.01],  'PG': [0.85, -8.81],  
            'CSCO': [0.88, 18.56],  'VZ': [0.9, 2.16], 
            'PFE': [0.92, 13.96],  'HD': [0.97, 3.2],  
            'INTC': [1.0, 2.61],  'T': [1.01, -15.19],  
            'V': [1.02, 24.0],  'UNH': [1.02, 19.32],  
            'WFC': [1.05, -3.59],  'CVX': [1.05, -5.77],  
            'BAC': [1.15, 4.27],  'JNJ': [1.41, -5.58],  
            'GOOGL': [1.46, 17.84],  'GOOG': [1.47, 17.03],  
            'BRK.B': [1.5, 4.54],  'XOM': [1.52, -6.87],  
            'JPM': [1.53, 7.66],  'FB': [2.02, 0.91], 
            'AMZN': [2.96, 62.75], 'MSFT': [3.28, 26.61],
            'AAPL': [3.94, 26.01]}
                                                                                                                                                                                                                                                                                      3.59],  'CVX': [1.05, -5.77],  'BAC': [1.15, 4.27],  'JNJ': [1.41, -5.58],  'GOOGL': [1.46, 17.84],  'GOOG': [1.47, 17.03],  'BRK.B': [1.5, 4.54],  'XOM': [1.52, -6.87],  'JPM': [1.53, 7.66],  'FB': [2.02, 0.91], 'AMZN': [2.96, 62.75], 'MSFT': [3.28, 26.61], 'AAPL': [3.94, 26.01]}

                                                                                                                                                                                                                                                                                      3.59],  'CVX': [1.05, -5.77],  'BAC': [1.15, 4.27],  'JNJ': [1.41, -5.58],  'GOOGL': [1.46, 17.84],  'GOOG': [1.47, 17.03],  'BRK.B': [1.5, 4.54],  'XOM': [1.52, -6.87],  'JPM': [1.53, 7.66],  'FB': [2.02, 0.91], 'AMZN': [2.96, 62.75], 'MSFT': [3.28, 26.61], 'AAPL': [3.94, 26.01]}
​

""" As you can see, data structures are very useful in collecting, storing and working with more information than simple strings or integers.
You will soon learn how to use dictionary methods to perform tasks, such as pull values from keys, 
sort values by keys, add values to the dictionary, and many other tasks that make data structures critical for data science.
 """

print(VINIX['C'])
