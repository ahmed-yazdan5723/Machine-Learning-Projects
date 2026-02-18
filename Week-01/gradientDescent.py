import math, copy
import numpy as np
import matplotlib.pyplot as plt

# Load our data set
x_train = np.array([1.0, 2.0])   #features
y_train = np.array([300.0, 500.0])   #target value

def compute_cost(x,y,w,b):
    m = x_train.shape[0]
    cost_sum = 0
    for i in range(m):
        f_wb = w*x[i] + b
        cost = (f_wb - y[i])**2
        cost_sum += cost
    total_cost = (1/(2*m))*cost_sum
    return total_cost

# cost function, J(w,b) = 1/2m*sum of(y'^i - y^i)^2
# w = w - alpha*d/dw(J(w,b))
# b = b - alpha*d/db(J(w,b))

# d/db(J(w,b)) = 1/m*summession()