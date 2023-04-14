# Kolmogorov-Smirnov Test

import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

df = pd.read_excel(r'../docs/non_parametric_methods.xlsx',
                   sheet_name = 'Лист3')
print(df, '\n')

x = np.array(df['sample1'].dropna())
y = np.array(df['sample2'].dropna())
print('x = ', x, '\ny = ', y, '\n')

stat, p = ks_2samp(x, y)
print('KS = %.3f, p = %.3f' % (stat, p))
