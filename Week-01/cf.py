import numpy as np

# Training datasets
x_train = np.array([1.0,2.0])
y_train = np.array([300,500])
w = 200
b = 100
def compute_cost(x,y,w,b):
    m = x_train.shape[0]
    cost_sum = 0
    for i in range(m):
        f_wb = w*x[i] + b
        cost = (f_wb - y[i])**2
        cost_sum += cost
    total_cost = (1/(2*m))*cost_sum
    return total_cost

print(f"when w={w}, b={b}: System error = {compute_cost(x_train, y_train, w, b)}")

    
