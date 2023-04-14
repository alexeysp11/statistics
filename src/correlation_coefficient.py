# Pearson correlation coefficient

import pandas as pd
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
from scipy import stats
import math

class CorrelationAnalysis: 
    def read_data(self):
        # get and print out input data 
        df = pd.read_excel(r'../data/nonparametric.xlsx',
                           sheet_name = 'Лист5')
        print('INPUT DATA:')
        print(df, '\n')
        
        # remember input data 
        self.x = np.array(df['x'])
        self.y = np.array(df['y'])


    # calculate correlation coefficients
    def calc_coef(self):
        # number of elements in input array
        n = len(self.x)
        
        # Pearson correlation coefficient
        r, r_pvalue = stats.pearsonr(self.x, self.y)
        
        # Spearman's rank correlation coefficient 
        rho, rho_pvalue = stats.spearmanr(self.x, self.y)

        # Student's t value
        t = r * math.sqrt((n-2)/(1-r**2))
        t_pvalue = stats.t.sf(np.abs(t), n-1)*2  # two-sided pvalue = Prob(abs(T)>t)

        # Fisher's F value
        f = (r**2 * (n-2)) / (1 - r**2)
        f_pvalue = stats.f.sf(np.abs(f), n-1, n-1)

        # round values for printing out a table
        r, r_pvalue = round(float(r), 3), round(float(r_pvalue), 3)
        rho, rho_pvalue = round(float(rho), 3), round(float(rho_pvalue), 3)
        t, t_pvalue = round(float(t), 3), round(float(t_pvalue), 3)
        f, f_pvalue = round(float(f), 3), round(float(f_pvalue), 3)

        # making a table
        list_for_table = [['stat', r, rho, t, f],
                        ['p-value', r_pvalue, rho_pvalue, t_pvalue, f_pvalue]]
        headers_table = ['', 'Pearson', 'Spearman', 'Student', 'Fisher']
        print('CORRELATION ANALYSIS:')
        print(tabulate(list_for_table, headers=headers_table))


    def draw_data(self):
        # initialize self.x and self.y as x and y respectively 
        x = self.x
        y = self.y
        
        # Scatter plot
        plt.scatter(x, y)
        plt.title('Scatter plot')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


def main():
    # Declare an instance correlation as a class Slope_Regression
    correlation = CorrelationAnalysis()
    
    # Call ReadData() method of correlation instance to get input data
    correlation.read_data()
    correlation.calc_coef()

    # draw all data
    correlation.draw_data()


if __name__ == '__main__':
    main()
