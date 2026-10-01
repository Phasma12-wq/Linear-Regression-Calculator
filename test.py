import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv')

def calc_xy_arr(data_x, data_y, row_count):

    xy_arr = []
    
    for n in range(row_count):
        xy_arr.append(data_x[n] * data_y[n])

    return xy_arr

def calc_x2_arr(data_x, row_count):

    xy_arr = []
    
    for n in range(row_count):
        xy_arr.append(data_x[n] * data_x[n])

    return xy_arr

def calc_y2_arr(data_y, row_count):

    xy_arr = []
    
    for n in range(row_count):
        xy_arr.append(data_y[n] * data_y[n])

    return xy_arr

def calc_b0(sum_x, sum_y, sum_x2, sum_xy, row_count):
    return round(((sum_y * sum_x2)-(sum_x * sum_xy))/((row_count * sum_x2) - (sum_x * sum_x)),4)

def calc_b1(sum_x, sum_y, sum_x2, sum_xy, row_count):
    return round((((row_count*sum_xy)-(sum_x*sum_y))/((row_count*sum_x2)- (sum_x * sum_x))),4)

def calc_value_from_x(b0, b1, x_value):
    return b0 + b1 * x_value

def calc_value_range_from_x(b0, b1, range_start, range_end):
    range_arr = []
    
    for x in range(range_start, (range_end+1)):
        result = b0 + b1 * x

        result_arr = [x, result]

        range_arr.append(result_arr)

    return range_arr

data_x = df["x"].to_numpy()
print(data_x, "\n")

data_y = df["y"].to_numpy()
print(data_y, "\n")

row_count = len(df.index)


sum_x = np.sum(data_x)
sum_y = np.sum(data_y)

xy_arr = calc_xy_arr(data_x, data_y, row_count)
sum_xy = np.sum(xy_arr)

x2_arr = calc_x2_arr(data_x, row_count)
sum_x2 = np.sum(x2_arr)

y2_arr = calc_y2_arr(data_y, row_count)
sum_y2 = np.sum(y2_arr)

print("Sum of x: ", sum_x, "\nSum of y: ", sum_y, "\nSum of x*y: ", sum_xy, "\nSum of x^2: ", sum_x2, "\nSum of y^2: ", sum_y2, "\n")

b0 = calc_b0(sum_x, sum_y, sum_x2, sum_xy, row_count)
b1 = calc_b1(sum_x, sum_y, sum_x2, sum_xy, row_count)

print("b0: ", b0, "\nb1: ", b1, "\n")
print("function: f(x) = ", b0, " + ", b1, "x")


#b0, b1 = np.polyfit(x, y, 1)

plt.plot(data_x, data_y, "o")

plt.plot(data_x, b1 * data_x + b0)
plt.show()



#predicted f(x) value from x value = 252
x_value = calc_value_from_x(b0, b1, 5)

print("f(252) = ", x_value)


#predicted f(x) value from x value range  50 to 100

range_values = calc_value_range_from_x(b0, b1, 0, 100)

for value in range_values:
    print(value[0], " ", value[1])