# Abbe Test

import pandas as pd
import numpy as np

df = pd.read_excel(r'non_parametric_methods.xlsx',
                   sheet_name = 'Лист1')
data = np.matrix(df)
print(data, '\n')

n = len(data)

SSE = 0
for i in range(n):
    sq_error = (data[i] - np.mean(data))**2
    SSE = SSE + sq_error
S = SSE / (n-1)

SS = 0
for i in range(n - 1):
    sq = (data[i+1] - data[i])**2
    SS = SS + sq
Q = SS / (2*(n-1))

print('S = ', float(S))
print('Q = ', float(Q))
print('q = ', float(Q / S))
