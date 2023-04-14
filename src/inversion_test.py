# Inversion Test

import pandas as pd
import numpy as np

df = pd.read_excel(r'../data/nonparametric.xlsx',
                   sheet_name = 'Лист1')
data = np.matrix(df)
print(data, '\n')

inversion = 0
for i in range(len(data)-1):
    a = 0
    for j in range(i+1, len(data)):
        if data[i] > data[j]:
            a = a + 1
            inversion = inversion + 1
    print('A[', i+1, '] = ', a)

print('\nTotal A = ', inversion)
