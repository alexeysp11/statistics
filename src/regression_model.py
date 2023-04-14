# Regression model 

import pandas as pd
import numpy as np
from scipy import linalg
from scipy import interpolate
import matplotlib.pyplot as plt


class RegrssionModel:
    def read_data(self):
        # get data from a file and display it
        df = pd.read_excel(r'C:\Users\User\Desktop\university\ФОПИ\6 семестр\расчеты.xlsx',
                           sheet_name = 'Регрессия_Тензорезисторы_1')
        print('INPUT DATA:')
        print(df, '\n')
        
        # "remember" data with no NaN
        self.x = np.array(df['x'].dropna())
        self.y1 = np.array(df['y_1'].dropna())
        self.y2 = np.array(df['y_2'].dropna())


    def least_squares(self):
        # redefine variables to reduce the time on typing
        x, y1, y2 = self.x, self.y1, self.y2

        # use polyfit to get linear regression coefficients
        self.linear_1 = np.polyfit(x, y1, 1)
        self.linear_2 = np.polyfit(x, y2, 1)

        # print out linear regression coefficients
        print('LINEAR REGRESSION COEFFICIENTS:')
        print('Linear regression 1: %.3f * x + %.3f'
              %(self.linear_1[0], self.linear_1[1]))
        print('Linear regression 2: %.3f * x + %.3f'
              %(self.linear_2[0], self.linear_2[1]))
        


    def plot_data(self):
        # redefine variables to reduce the time on typing
        x, y1, y2 = self.x, self.y1, self.y2
        linear_1 = self.linear_1
        linear_2 = self.linear_2
        
        # Scatter plot
        fig = plt.figure()
        scatter = fig.add_subplot(121)
        scatter.plot(x, y1, 'bo', label='K_F Higher')
        scatter.plot(x, y2, 'ro', label='K_F Lower')
        plt.xlabel('Relative strain, *10^3')
        plt.ylabel('Transfer function, *10^3')
        plt.title('Scatter plot')
        plt.grid()
        plt.legend()

        # Regression models
        regres = fig.add_subplot(122)
        regres.plot(x, y1, 'bo', label='K_F верхний (экспериментальные)')
        regres.plot(x, y2, 'ro', label='K_F нижний (экспериментальные)')
        regres.plot(x, linear_1[0]*x + linear_1[1], 'b-',
                    label='K_F верхний (предсказанные)')
        regres.plot(x, linear_2[0]*x + linear_2[1], 'r-',
                    label='K_F нижний (предсказанные)')
        plt.xlabel('Относительная деформация, *10^3')
        plt.ylabel('Функция преобразования, *10^3')
        plt.title('Линейная регрессия')
        plt.grid()
        plt.legend()

        # plot all
        plt.show()


def main():
    regression = RegrssionModel()
    regression.read_data()
    regression.least_squares()
    
    # plot all data 
    regression.plot_data()

if __name__ == '__main__':
    main()
