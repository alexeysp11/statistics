# Work 1.
# Abbe test, runs test and inversion test


import pandas as pd
import numpy as np
from scipy.stats import shapiro
from matplotlib import pyplot


class StatisticalMethods:
    # Read data from Excel file 
    def __init__(self):
        # rename sheet_name! 
        df = pd.read_excel(r'../data/nonparametric.xlsx', sheet_name = 'Лист1')
        self.data = np.array(df)

    # Check if a dataset is well modeled by a normal distribution 
    def preliminary_analysis(self):
        # initialize data 
        data = self.data
        print(data, '\n')
        num_elem = len(data)

        # normality testing
        # is it necessary for runs and inversion tests to check normality? 
        if (num_elem >= 3 and num_elem <= 50):
            print('NORMALITY TESTING')
            print('We use Shapiro-Wilk Test because number of elements ranges from 3 to 50')
            stat, pvalue = shapiro(data)
            print('W = %.3f, p-value = %.3f' % (stat, pvalue))

        # conclusion about normality
        alpha = 0.05
        if pvalue >= alpha:
            print('Normal distribution')
        else:
            print('Not normal distribution')

        # histogram plot
        # legends and title!
        pyplot.hist(data, edgecolor = 'black')
        pyplot.show()

    # Print result of the methods in a table
    def print_result(self):
        # either you leave this way or you include tables into this program!
        print('\nYou should use statistical tables to interpret calculated values!')


# terminology!
class AbbeTest(StatisticalMethods):
    def abbe_test(self):
        # initialize data 
        data = self.data
        n = len(data)

        # unbiased estimator of a sample variance
        unbiased_var = np.var(data, ddof=1)

        # Calculate the sum of squared differences (see at README.md)
        # SS is total sum of squares, sq is local sum of squares
        SS = 0   
        for i in range(n - 1):
            sq = (data[i+1] - data[i])**2 
            SS = SS + sq
        Q = SS / (2*(n-1))

        stat = Q / unbiased_var

        # print out results 
        print('S = ', float(unbiased_var))
        print('Q = ', float(Q))
        print('q = ', float(stat))


class InversionTest(StatisticalMethods):
    def inversion_test(self):
        # initialize data
        data = self.data

        # calculations
        total_inversion = 0
        for i in range(len(data)-1):
            local_inversion = 0
            for j in range(i+1, len(data)):
                if data[i] > data[j]:
                    local_inversion = local_inversion + 1
                    total_inversion = total_inversion + 1
            print('A[', i+1, '] = ', local_inversion)
            
        print('Total A = ', total_inversion)


class RunsTest(StatisticalMethods):
    # expressions like this: value =+ 1!
    def runs_test(self, data):
        # visualize sorted list and calculate a median 
        sorted_list = np.reshape(np.sort(data, axis=None),
                      (len(data),1))
        print(sorted_list)
        median = np.median(data)

        # calculations in a row (relative to initial data)
        row = ''
        positive = 0
        negative = 0
        for i in range(len(data)):
            if data[i] >= median:
                row = row + '+ '
                positive = positive + 1
            else:
                row = row + '- '
                negative = negative + 1

        # calculate statistics 
        stat = 1
        for i in range(len(data) - 1):
            if ((data[i] >= median and data[i + 1] < median)
                or (data[i] < median and data[i + 1] >= median)):
                stat = stat + 1
        return row, median, positive, negative, stat

    # Print out calculations of Runs test
    def print_out(self):
        # call runs_test function and initialize result 
        row, median, positive, negative, stat = self.runs_test(self.data)

        # print out conclusion
        print('%s\nmedian = %.3f\np = %d\nn = %d\nr = %d'
              % (row, median, positive, negative, stat))


def main():
    print('INITIAL DATA:')
    stat_methods = StatisticalMethods()
    stat_methods.preliminary_analysis()
    
    print('\nABBE TEST')
    abbe = AbbeTest()
    abbe.abbe_test()
    
    print('\nINVERSION TEST')
    inv_test = InversionTest()
    inv_test.inversion_test()
    
    print('\nWALD-WOLFOWITZ RUNS TEST')
    runs = RunsTest()
    runs.print_out()

    # conclusions
    stat_methods.print_result()


if __name__ == '__main__':
    main()
