import numpy as np

# Training datasets
x_train = np.array([1.0,2.0])
y_train = np.array([300,500])

# Defining the cost function
def compute_cost(x,y,w,b):
    m = x_train.shape[0] #Number of training examples
    cost_sum = 0
    for i in range(m):
        f_wb = w*x[i] + b
        cost = (f_wb - y[i]) ** 2
        cost_sum += cost

    total_cost = (1/(2*m))*cost_sum
    return total_cost

