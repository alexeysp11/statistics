# Normality Test

import pandas as pd
import numpy as np
from scipy.stats import shapiro
from matplotlib import pyplot

df = pd.read_excel(r'../docs/non_parametric_methods.xlsx',
                   sheet_name = 'Лист1')
data = np.matrix(df)
print(data, '\n')

# Shapiro-Wilk Test
stat, p = shapiro(data)
print('W = %.3f, p = %.3f' % (stat, p))

# histogram plot
pyplot.hist(data, edgecolor = 'black')
pyplot.show()

##alpha = np.array([0.01, 0.05, 0.1])
### interpret
##for i in range(len(alpha)):
##    if p > alpha[i]:
##        conclusion = 'Fail to reject H0'
##    else:
##        conclusion = 'Reject H0'
##    print('alpha = ' + str(alpha[i]) + ': ' +
##                conclusion)
