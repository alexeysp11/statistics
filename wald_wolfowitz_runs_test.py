# Wald-Wolfowitz runs test

import pandas as pd
import numpy as np


def calculateMedian(list):
    data = sorted(list)
    n = len(data)
    if n == 0:
        return None
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i - 1] + data[i]) / 2


def runs_test(data):
    row = ''
    positive = 0
    negative = 0
    sorted_list = np.reshape(np.sort(data, axis=None),
                  (len(data),1))
    print(sorted_list, '\n')
    median = calculateMedian(data)
    for i in range(len(data)):
        if data[i] >= median:
            row = row + '+ '
            positive = positive + 1
        else:
            row = row + '- '
            negative = negative + 1
    r = 1
    for i in range(len(data) - 1):
        if ((data[i] >= median and data[i + 1] < median)
            or (data[i] < median and data[i + 1] >= median)):
            r = r + 1
    return row, median, positive, negative, r


def main(): 
    df = pd.read_excel(r'non_parametric_methods.xlsx',
                       sheet_name = 'Лист1')
    data = np.matrix(df)

    print(data, '\n')

    row, median, positive, negative, r = runs_test(data)
    print('%s\n\nmedian = %.3f\np = %d\nn = %d\nr = %d'
          % (row, median, positive, negative, r))

    
if __name__ == '__main__':
    main()
    
