"""
function that splits data into train, val and test sets

"""

import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split

print ('Read/upload X dataframe. ')
print ('Read/upload y dataframe')
train_size=float(input('What is the train size in decimal form? '))
val_size=float(input('What is the validation size in decimal form? '))
test_size=float(input('What is the test size in decimal form? '))
random_seed=int(input('Random seed? '))

X = pd.DataFrame({'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku', 'A', 'B', 'C', 'D', 'E'], 
        'Age':[27, 24, 22, 32, 15, 45, 32, 61, 23, 40], 
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida', 'Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'], 
        'Qualification':['Msc', 'MA', 'MCA','Msc', 'MA', 'MCA', 'Phd', '10th', 'Phd', '10th']})

y = pd.DataFrame({'result': [1, 0, 1, 1, 1, 0, 0, 1, 0, 0]})

def train_val_test_split (X, y, train_size, val_size, test_size, random_seed, shuffle=True):

    assert train_size + val_size + test_size ==1

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, 
        test_size = test_size, 
        random_state = random_seed, 
        shuffle= shuffle
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, 
        test_size= val_size/(train_size + val_size), 
        random_state=random_seed, 
        shuffle= shuffle)
    
    print('')
    print(X)
    print('')
    print(y)
    
    return X_train, X_val, X_test, y_train, y_val, y_test

#print(train_val_test_split(X, y, train_size, val_size, test_size, random_seed, shuffle=True))
print('X_train', X_train)