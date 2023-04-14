import pandas as pd
import numpy as np
from scipy.stats import ranksums
import math

df = pd.read_excel(r'../docs/non_parametric_methods.xlsx',
                           sheet_name = 'Лист3')
print(df, '\n')

x = np.matrix(df['sample1'].dropna())
y = np.matrix(df['sample2'].dropna())
print('x = ', x, '\ny = ', y, '\n')

x = np.transpose(x)
y = np.transpose(y)
stat, p = ranksums(x, y)
##print('T = %.3f, p = %.3f' % (stat, p))

smaller = len(x)
larger = len(y)
total = smaller + larger

W_bar = stat/smaller
numenator = W_bar - smaller*(total + 1) + 1/(2*smaller)
denominator = math.sqrt(smaller*larger*(total + 1)/3)
z_score = numenator/denominator
print('z-score* = %.3f' % z_score)
