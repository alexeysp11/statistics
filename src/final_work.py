"""
Prepare for exam stats 6th season
Here we use wilcoxon, hodges-lehmann, ks and spearman tests. 
"""


import pandas as pd
import numpy as np
from scipy import stats
from tabulate import tabulate
import matplotlib.pyplot as plt


class DataAnalysis:
    def read_data(self):
        # get data from a file and display it
        df = pd.read_excel(r'../data/nonparametric.xlsx',
                           sheet_name = 'Подготовка к зачету')
        print('INPUT DATA:')
        print(df, '\n')
        
        # "remember" data with no NaN
        self.x = np.array(df['x'].dropna())
        self.y = np.array(df['y'].dropna())


    # Hodges-Lehmann estimator
    def hodges_lehmann(self):
        # initialize sizes of samples
        x, y = self.x, self.y
        size_x, size_y = len(x), len(y)
        total_size = size_x + size_y

        # Get an array of differences between x and y
        shape_delta_vector = (size_x * size_y, 1)
        delta_vector = np.ones(shape_delta_vector)
        delta = 0
        k = 0
        for i in range(size_x):
            for j in range(size_y):
                delta_vector[k] = y[j] - x[i]
                k = k + 1

        # print an array of differences in a form of matrix
        shape = (size_x, size_y)
        delta_matrix = np.reshape(delta_vector, shape)

        # get an estimate of location parameter
        delta_hat = float(self.calculateMedian(delta_vector))
        return delta_hat


    def calculateMedian(self, List):
        data = sorted(List)
        n = len(data)
        if n == 0:
            return None
        if n % 2 == 1:
            return data[n // 2]
        else:
            i = n // 2
            return (data[i - 1] + data[i]) / 2 


    # analyze data
    def analysis(self):
        x, y = self.x, self.y
        
        # wilcoxon rank sum test
        ranksums_stat, ranksums_pvalue = stats.ranksums(x, y)        
        # hodges-lehmann estemator (no p value)
        hodges_lehmann_stat = self.hodges_lehmann()
        # ks test
        ks_stat, ks_pvalue = stats.ks_2samp(x, y)
        # spearman test
        spearman_stat, spearman_pvalue = stats.spearmanr(x, y)

        # round values for printing out a table
        ranksums_stat, ranksums_pvalue = round(float(ranksums_stat), 3), round(float(ranksums_pvalue), 3)
        hodges_lehmann_stat = round(float(hodges_lehmann_stat), 3) 
        ks_stat, ks_pvalue = round(float(ks_stat), 3), round(float(ks_pvalue), 3)
        spearman_stat, spearman_pvalue = round(float(spearman_stat), 3), round(float(spearman_pvalue), 3)

        # making a table
        list_for_table = [['stat', ranksums_stat, hodges_lehmann_stat, ks_stat, spearman_stat],
                        ['p-value', ranksums_pvalue, 'none', ks_pvalue, spearman_pvalue]]
        headers_table = ['', 'Rank Sum', 'Hodges-Lehmann', 'KS', 'Spearman']
        print('DATA ANALYSIS:')
        print(tabulate(list_for_table, headers=headers_table))


    def plot_data(self):
        # redefine variables to reduce the time on typing
        x, y = self.x, self.y
        
        # Box plot
        fig = plt.figure('Input data')
        boxplot = fig.add_subplot(121)
        boxplot.boxplot((x,y), labels=('x','y'))
        plt.title('Box plot')
        plt.grid()
        
        # Scatter plot
        scatter = fig.add_subplot(122)
        scatter.scatter(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Scatter plot')
        plt.grid()
   
        plt.show()


def main():
    # da (short of data analysis) is an instance of DataAnalysis class
    da = DataAnalysis()
    da.read_data()
    da.analysis()
    
    # plot all data 
##    da.plot_data()


if __name__ == '__main__':
    main()
