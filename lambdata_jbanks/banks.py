

import pandas
from pandas import DataFrame
from lambdata_jbanks.mod import enlarge

df=DataFrame({"a":[2,4,6], "b":[1,3,5]})
print (df.head())


print ("Hello")

x= int(input("enter an integer"))
print(enlarge(x))