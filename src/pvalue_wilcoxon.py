# Count p-value for Wilcoxon test

import pandas as pd
import numpy as np

class P_Value:
    def read_data():
        df = pd.read_excel(r'../docs/non_parametric_methods.xlsx',
                           sheet_name = 'Лист3')
        print(df, '\n')

        x = np.matrix(df['sample1'].dropna())
        y = np.matrix(df['sample2'].dropna())
        print('x = ', x, '\ny = ', y, '\n')

        x = np.transpose(x)
        y = np.transpose(y)
        

    def factorial(n):
        fact = 1
        for i in range(1, n+1): 
            fact = fact * i  
        return fact

    def count_k(sample1, sample2):
        return k

    def pvalue(sample1, sample2):
        n_1 = len(sample1)
        n_2 = len(sample2)
        total_n = n_1 + n_2
        if n_1 < n_2:
            smaller = n_1
            larger = n_2
        else:
            smaller = n_2
            larger = n_1
        print('n (smaller): ', smaller)
        print('m (larger): ', larger)
        print('N (total): ', total_n)
        
        # Without repeats
        combinations = factorial(total_n)/(
            factorial(smaller)*
                        factorial(total_n -smaller))
        print(combinations)
        # k = 1290, p = 0,01396
        k = count_k(sample1, sample2)
    

def main():
    df = pd.read_excel(r'../docs/non_parametric_methods.xlsx',
                           sheet_name = 'Лист3')
    print(df, '\n')

    x = np.matrix(df['sample1'].dropna())
    y = np.matrix(df['sample2'].dropna())
    print('x = ', x, '\ny = ', y, '\n')
    
    smaller = 9
    larger = 10
    total = smaller + larger
    combinations = 92378
    combinations_smaller = 91361
    print('n (smaller): ', smaller)
    print('m (larger): ', larger)
    print('N (total): ', total)
    print('Total combinations: ', combinations)
    print('Total combinations (rank sums smaller 118): ', combinations_smaller)
    print('p = %.3f' % (combinations_smaller/combinations))

if __name__ == '__main__':
    main()
