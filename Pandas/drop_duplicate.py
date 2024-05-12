import pandas as pd
import numpy as np


data = np.array([[1,2,3,3,4,4,4,5], [10,20,30,40,50,60, 70, 80]])
data = data.T


df = pd.DataFrame(data, columns=['a','b'])
print(df)
print(df.sort_values('b', ascending=False).drop_duplicates('a'))