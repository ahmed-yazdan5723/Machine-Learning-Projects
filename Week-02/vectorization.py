import numpy as np
import time

# NumPy routines which allocate memory and fill arrays with value
# a = np.zeros(4);                
# print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

# a = np.zeros((4,));             
# print(f"np.zeros(4,) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

# a = np.random.random_sample(4); 
# print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")


# NumPy routines which allocate memory and fill arrays with value but do not accept shape as input argument
# a = np.arange(4.);              
# print(f"np.arange(4.): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

# a = np.random.rand(4);          
# print(f"np.random.rand(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")




#vector indexing operations on matrices
# a = np.arange(6).reshape(-1, 2)   #reshape is a convenient way to create matrices
# print(f"a.shape: {a.shape}, \na= {a}")

# #access an element
# print(f"\na[2,0].shape:   {a[2, 0].shape}, a[2,0] = {a[2, 0]},     type(a[2,0]) = {type(a[2, 0])} Accessing an element returns a scalar\n")

# #access a row
# print(f"a[2].shape:   {a[2].shape}, a[2]   = {a[2]}, type(a[2])   = {type(a[2])}")





#vector 2-D slicing operations
a = np.arange(20).reshape(-1, 10)
print(f"a = \n{a}")

#access 5 consecutive elements (start:stop:step)
print("a[0, 2:7:1] = ", a[0, 2:7:1], ",  a[0, 2:7:1].shape =", a[0, 2:7:1].shape, "a 1-D array")

#access 5 consecutive elements (start:stop:step) in two rows
print("a[:, 2:7:1] = \n", a[:, 2:7:1], ",  a[:, 2:7:1].shape =", a[:, 2:7:1].shape, "a 2-D array")

# access all elements
print("a[:,:] = \n", a[:,:], ",  a[:,:].shape =", a[:,:].shape)

# access all elements in one row (very common usage)
print("a[1,:] = ", a[1,:], ",  a[1,:].shape =", a[1,:].shape, "a 1-D array")
# same as
print("a[1]   = ", a[1],   ",  a[1].shape   =", a[1].shape, "a 1-D array")
