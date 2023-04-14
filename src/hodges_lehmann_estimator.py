# Hodges-Lehmann estimator

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# calculate median for an estimate of location
# parameter in analitical method 
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


# colors for graphical confidence intervals 
def switch_color(k):
    if k == 0:
        return 'k'
    elif k == 1:
        return 'r'
    else:
        return 'g--'
 

def main():
    
    # READ DATA
    df = pd.read_excel(r'../docs/non_parametric_methods.xlsx',
                       sheet_name = 'Лист3')
    print(df, '\n')

    x = np.matrix(df['sample1'].dropna())
    y = np.matrix(df['sample2'].dropna())
    print('x = ', x, '\ny = ', y, '\n')

    # transpose initial matrix because algorithm
    # doesn't work without it. I don't know why
    x = np.transpose(x)
    y = np.transpose(y)


    # ANALITICAL METHOD

    # initialize sizes of samples 
    size_x = len(x)
    size_y = len(y)
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
    print(delta_matrix, '\n')

    # get an estimate of location parameter
    delta_hat = float(calculateMedian(delta_vector))
    print('delta = ', delta_hat)

    # critical values for confidence interval for estimation
    w = [114, 111] # critical values for .05 and .10 p-values
    p = [0.05, 0.10]
    
    # define C array that helps us to deifne optimal critical
    # statistics for graphical method
    medium = size_x*size_y/2
    C = np.ones((len(w) + 1, 2))
    C[0] = [medium, medium]
    k = 1

    # get bounds of confidence interval for estimation
    for i in range(len(w)):
        C_a = int(size_y*(2*size_x + size_y + 1)/2 + 1 - w[i])
        left = float(delta_vector[C_a])
        C_b = size_x * size_y + 1 - C_a
        right = float(delta_vector[C_b])
        C[k] = [C_a, C_b]
        k = k + 1
        print('Confidence interval (p = %.2f): %.1f < %.1f < %.1f'
              %(p[i], left, delta_hat, right))


    # GRAPHICAL METHOD
    
    # define points of differences array
    points = np.ones((size_x * size_y, 2))
    k = 0
    
    # plot points
    for i in range(size_x):
        for j in range(size_y):
            plt.plot(x[i], y[j], 'bo')
            points[k] = [x[i], y[j]]
            k = k + 1

    # we need to draw a line y=kx+b, where k=tg(45deg)=1, so:
    intercept = 0 # by default
    x_plt = np.arange(max(x) + 5)

    # Declaire critical number of points that was defined
    # empirically with the help of C arrray,
    # because exact critical number of points can't be counted
    # exactly with any steps. As a result this programm stucks
    critical_num_points = np.matrix([[45, 45], [31, 60],[37, 56]])
    num_rows, num_cols = critical_num_points.shape
    
    # declaire intercepts array
    intercepts = np.ones((num_rows, 2))
    ind_high, ind_low = 0, 0

    # draw lines for each confidence interval 
    for cols in range(num_cols):
        for rows in range(num_rows):
            
            # Count number of points above critical statistics: 
            # while number of points above the line is not equal
            # to critical_statistics* (number of points that should
            # be above the line), we check their number and adjust
            # intercept to make the number smaller
            above = 0
            while(above != critical_num_points[rows, cols]):  
                above = 0
                for i in range(len(points)):
                    # ponits[x, y], so if y > x + intercept, then
                    # point is above the line 
                    if (points[i,1] > points[i,0] + intercept):
                        above = above + 1

                # if number of points that are above the line
                # is bigger than critical statistics, then we adjust intercept
                # and repeat while loop to check the number of points
                # above the line
                if (above > critical_num_points[rows, cols]):        
                    intercept = intercept + 0.5
                elif (above < critical_num_points[rows, cols]):
                    intercept = intercept - 0.5

            # define each intercept
            intercepts[rows, cols] = intercept
            
            # draw different interval in different colors
            plt.plot(x_plt, x_plt + intercept, switch_color(rows))

    # Print out intercepts and plot 
    print('Intercepts = \n', intercepts)
    plt.show()


if __name__ == '__main__':
    main()
