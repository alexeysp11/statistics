# Read Excel file that contains some dataset we need to analyze 

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

import matplotlib.pyplot as plt

# So let's try to draw histogram of distribution 
df = pd.read_excel(r'C:\Users\User\Desktop\python\some_dataset_for pandas_1.xlsx', sheet_name = 'Лист1')

plt.hist(df['Data'], color = 'blue', edgecolor = 'black')
plt.show()

print(df.describe())


