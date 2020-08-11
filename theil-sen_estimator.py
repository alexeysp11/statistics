# Theil-Sen Estimator

import pandas as pd
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
from scipy import stats


class Slope_Regression: 
    def ReadData(self):
        # get and print out input data 
        df = pd.read_excel(r'non_parametric_methods.xlsx',
                           sheet_name = 'Лист4')
        print('INPUT DATA:')
        print(df, '\n')
        
        # remember input data 
        x = np.array(df['x'])
        y = np.array(df['y'])
        self.x = x.reshape((len(x), 1))
        self.y = y.reshape((len(y), 1))


    # H_0: slope=0, H_A: slope != 0
    def IsEqualHypothesis(self):
        # find differences of actual and expected y if slope = 0
        slope = 0
        n = len(self.x)
        D = np.ones((n, 1))
        for i in range(n):
            D[i] = self.y[i] - slope * self.x[i]
        self.D = D
        
        # count number of elements in dif array
        num_dif = 0
        for i in range(n):
            for j in range(n):
                if i < j:
                    num_dif = num_dif + 1
        self.num_dif = num_dif
        
        # create D[j]-D[i] (or dif array)
        dif = np.ones((num_dif, 1))
        ind = 0
        for i in range(n):
            for j in range(n):
                if i < j:
                    dif[ind] = D[j] - D[i]
                    ind = ind + 1
        self.dif = dif

        # c(D[j]-D[i])
        c = np.ones((num_dif, 1))
        for i in range(len(dif)):
            if dif[i] > 0:
                c[i] = 1
            elif dif[i] == 0:
                c[i] = 0
            else:
                c[i] = -1 

        # "remember" some data that we need in the future
        # and execute PrintOutHypothesis() method
        self.c = c
        self.sum_c = int(sum(c))
        self.PrintOutHypothesis()


    def TheilSenEsimator(self, alpha):
        # calculate Theil-Sen estimation 
        res = stats.theilslopes(self.y, self.x, alpha)
        print('%.2f confidence interval:' % alpha)
        print('slope: %.3f, intercept: %.3f, low: %.3f, up: %.3f' %(res[0], res[1], res[2], res[3]))
        return res

    
    def Draw(self):
        # initialize self.x and self.y as x and y respectively 
        x = self.x
        y = self.y
        
        # Scatter plot
        plt.scatter(x, y)
        plt.title('Scatter plot')
        
        # Theil-Sen Estimator for some confidence interval
        # which is defined as alpha 
        print('\nDRAWING CONFIDENCE INTERVAL')
        alpha = 0.95
        res = self.TheilSenEsimator(alpha)
        
        # plot a data
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x, y, 'b.', label='Observed data')
        ax.plot(x, res[1] + res[0] * x, 'k-', label='Theil-Sen estimation')
        ax.plot(x, res[1] + res[2] * x, 'g--')
        ax.plot(x, res[1] + res[3] * x, 'g--', label='Upper and Lower bound')
        plt.grid()
        ax.legend()
        plt.title('Theil-Sen estimator (95% confidence interval)')
        plt.show()

    
    # PRINT OUT HYPOTHESIS TESTING DATA 
    def PrintOutHypothesis(self):
        # for more details of processing in this method,
        # look at IsEqualHypothesis() method
        print("HYPOTHESIS TESTING:")
        hypothesis_input = [(self.x, self.y, self.D)]
        print(tabulate(hypothesis_input, headers=["x", "y", "y - kx"]), '\n')

        # create a table of processed data 
        hypothesis_processing = [(self.dif, self.c)]
        print(tabulate(hypothesis_processing, headers=["D[j]-D[i]", "c(D[j]-D[i])"]), '\n')

        # print out all data that haven't been fitted in a table 
        print("num_dif: %d, C: %d\n" %(self.num_dif, self.sum_c))


def main():
    # Declare an instance slope_estimator as a class Slope_Regression
    slope_estimator = Slope_Regression()
    
    # Call ReadData() method of slope_estimator instance to get input data
    slope_estimator.ReadData()
    
    # Call IsEqualHypothesis() method of slope_estimator instance
    slope_estimator.IsEqualHypothesis()

    # Theil-Sen Estimator and confidence interval
    print('THEIL-SEN ESTIMATOR')
    alpha = [0.90, 0.95, 0.99]
    for i in range(len(alpha)):
        slope_estimator.TheilSenEsimator(alpha[i])
    
    # Draw plots of linear regression and Theil-Sen
    slope_estimator.Draw()


if __name__ == '__main__':
    main()
