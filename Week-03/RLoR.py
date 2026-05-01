import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=8)

'''
Steps to be done:
0. dataset and other variables
1. Gradient descent
2. Cost function
3. cost value + regularized cost
4. f(X) = sigmoid(np.dot(w,X) + b)
5. sigmoid(z) = 1 / 1 - np.exp(-z) DONE

dj_dw = 1/m * (f_wb_i - y[i])x[j] + lambda_/m * w[j]
'''

''' Defining functions '''
def sigmoid(z): 
    return 1 / (1 + np.exp(-z))

def compute_cost_logistic_reg(X, y, w, b, lambda_ = 1):
    # Defining the necessary variables
    m= X.shape[0]
    n = len(w)
    cost = 0.

    for i in range(m):
        z = np.dot(X[i],w) + b
        f_wb_i = sigmoid(z)
        f_wb_i = np.clip(f_wb_i, 1e-15, 1 - 1e-15)
        cost = cost + -y[i]*np.log(f_wb_i) - (1 - y[i])*np.log(1 - f_wb_i)
    
    cost = cost / m
    
    # Calculating regularized cost
    reg_cost = 0
    
    for j in range(n):
        reg_cost += (w[j]**2)
    
    reg_cost = (lambda_/(2*m)) * reg_cost
    
    # Total cost
    total_cost = cost + reg_cost
    return total_cost

def compute_gradient_logistic_reg(X, y, w, b, lambda_):
    m,n = X.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.0

    for i in range(m):
        f_wb_i = sigmoid(np.dot(X[i],w) + b)
        err_i = f_wb_i - y[i]
        for j in range(n):
            dj_dw[j] += err_i * X[i,j]
        
        dj_db += err_i
    dj_dw = dj_dw/m
    dj_db = dj_db/m

    # Regularizing
    for j in range(n):
        dj_dw[j] +=  (lambda_/m)*w[j]
    
    return dj_db, dj_dw 

np.random.seed(1)
X_tmp = np.random.rand(5,3)
y_tmp = np.array([0,1,0,1,0])
w_tmp = np.random.rand(X_tmp.shape[1])
b_tmp = 0.5
lambda_tmp = 0.7
dj_db_tmp, dj_dw_tmp =  compute_gradient_logistic_reg(X_tmp, y_tmp, w_tmp, b_tmp, lambda_tmp)

print(f"dj_db: {dj_db_tmp}", )
print(f"Regularized dj_dw:\n {dj_dw_tmp.tolist()}", ) 




