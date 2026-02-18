import numpy as np

x_train = np.array([1,2])
y_train = np.array([300,500])
w = 200
b = 100
m = x_train.shape[0]

# f_wb = w*x + b

def compute_model_output(x,w,b):
    f_wb = np.zeros(m)

    for i in range(m):
        f_wb = w*x[i] + b
    
    return f_wb
