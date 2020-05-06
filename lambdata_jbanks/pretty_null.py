"""
Prints out null values from a dataframe"

"""

import pandas as pd
import numpy as np
from pandas import DataFrame

df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                    'num_wings': [np.NaN, 0, 0, 0],
                    'num_specimen_seen': [10, np.NaN, 1, 8]},
                   index=['falcon', 'dog', 'spider', 'fish'])

#prints df
print(df)
print('')
#prints null values
null_df= pd.DataFrame((df.isnull().sum()), columns=['Null Freq'])
print(null_df)




