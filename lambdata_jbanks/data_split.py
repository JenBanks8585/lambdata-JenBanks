"""
function that splits data into train, val and test sets

"""

import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split

train_size=float(input('What is the train size in decimal form? '))
val_size=float(input('What is the validation size in decimal form? '))
test_size=float(input('What is the test size in decimal form? '))
random_seed=int(input('Random seed? '))


def train_val_test_split (X, y, train_size=train_size, val_size=val_size, test_size=test_size, random_seed=random_seed, shuffle=True):

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
    
    X_train=pd.DataFrame(X_train)
    X_val=pd.DataFrame(X_val)
    X_test=pd.DataFrame(X_test)
    y_train=pd.DataFrame(y_train)
    y_val=pd.DataFrame(y_val)
    y_test=pd.DataFrame(y_test)

    print('X_train') 
    print(X_train)
    print("")
    print('X_val')
    print(X_val)
    print("")
    print('X_test')  
    print(X_test)
    print("")
    print('y_train')  
    print(y_train)
    print("")
    print('y_val')  
    print(y_val)
    print("")
    print('y_test')  
    print(y_test)