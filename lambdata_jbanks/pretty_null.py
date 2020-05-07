"""
Prints out null values from a dataframe"

"""

import pandas as pd
import numpy as np
from pandas import DataFrame

def null_df(X):
  df_null= pd.DataFrame((X.isnull().sum()), columns=['Null Freq'])
  print(df_null)






