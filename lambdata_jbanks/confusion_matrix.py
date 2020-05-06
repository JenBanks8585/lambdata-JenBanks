"""
Plots confusion matrix of a 2 x 2 array"

"""

import pandas as pd
import numpy as np
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

# for index and column labels
Actual = ['Actual False', 'Actual True']
Predicted= ['Predicted False', 'Predicted True']

#User input
true_negative= int(input('What is the actual false and predicted false value? '))
false_positive=int(input('What is the actual false but predicted true value? '))
false_negative=int(input('What is the actual true but predicted false value? '))
true_positive= int(input('What is the actual true and predicted true value? '))

array= [[true_negative, false_positive],
        [false_negative, true_positive]]

cm=pd.DataFrame(array, 
                columns=[i for i in Predicted], 
                index= [i for i in Actual])

print(''*3)
print(cm)
print(''*3)
# Plotting
plt.figure(figsize=(10,7))
plt.title('Confusion Matrix')
sns.heatmap(cm, annot=True)