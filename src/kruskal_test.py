# Kruskal rank-signed test

import pandas as pd
import numpy as np
from scipy.stats import kruskal

df = pd.read_excel(r'../docs/non_parametric_methods.xlsx',
                   sheet_name = 'Лист3')
print(df, '\n')

x = np.matrix(df['sample1'].dropna())
y = np.matrix(df['sample2'].dropna())
print('x = ', x, '\ny = ', y, '\n')

x = np.transpose(x)
y = np.transpose(y)

stat, p = kruskal(x, y)
print('H = %.3f, p = %.3f' % (stat, p))
