# Importing libraries
import numpy as np

# Given Datasets
# x1 = 1
# y1 = 300
# x2 = 2
# y2 = 500

# Initializing training datasets
x_train = np.array([1.0, 2.0])
y_train = np.array([300,500])

# print(f"x_train = {x_train}")
# print(f"y_train = {y_train}")


# m is the number of training examples
m = x_train.shape[0]
print(f"Number of training examples is: {m}")

# Accessing i'th element of the training example
i = 0 # Change this to 1 to see (x^1, y^1)

x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")

# Initializing variables needed for the Linear Model
w = 200 #weight
b = 100 #bias

#Linear Model Function
def compute_model_output(x, w, b):
    f_wb = np.zeros(m)
    
    for i in range(m):
        f_wb[i] = w * x[i] + b
        
    return f_wb

# Applying the function, predict the price of a 1200sqft apartment
w1 = 200
b1 = 100
x_i = 1.2

cost_1200sqft = w1*x_i + b1
print(f"Cost of {x_i*1000}sqft apartment is: {cost_1200sqft} thousand dollars!")