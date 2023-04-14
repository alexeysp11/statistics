# Wilcoxon rank-sum test

import pandas as pd
import numpy as np
from scipy.stats import ranksums

def main():
    df = pd.read_excel(r'../data/nonparametric.xlsx',
                       sheet_name = 'Лист3')
    print(df, '\n')

    x = np.matrix(df['sample1'].dropna())
    y = np.matrix(df['sample2'].dropna())
    print('x = ', x, '\ny = ', y, '\n')

    x = np.transpose(x)
    y = np.transpose(y)

    stat, p = ranksums(x, y)
    print('T = %.3f, p = %.3f' % (stat, p))

if __name__ == '__main__':
    main()
