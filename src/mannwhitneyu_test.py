# Mann Whitney U test

import pandas as pd
import numpy as np
from scipy.stats import shapiro, mannwhitneyu
from matplotlib import pyplot

def shapiro_wilk_test(data):
    # Normality test
    stat, p = shapiro(data)
    print('W = %.3f, p = %.3f' % (stat, p))

    # histogram plot
    pyplot.hist(data, edgecolor = 'black')
    pyplot.show()


def main():
    df = pd.read_excel(r'../data/nonparametric.xlsx',
                       sheet_name = 'Лист3')
    print(df, '\n')

    x = np.matrix(df['sample1'].dropna())
    y = np.matrix(df['sample2'].dropna())
    print('x = ', x, '\ny = ', y, '\n')

    x = np.transpose(x)
    y = np.transpose(y)
    
##    # Shapiro-Wilk Normality Test
##    print('Normality test of X:')
##    shapiro_wilk_test(x)
##    print('Normality test of Y:')
##    shapiro_wilk_test(y)
    
    # Mann Whitney U test
    stat, p = mannwhitneyu(x, y)
    print('U = %.3f, p = %.3f' % (stat, p))

if __name__ == '__main__':
    main()
