import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([0., 1, 2, 3, 4, 5],dtype=np.longdouble)
y_train = np.array([0,  0, 0, 1, 1, 1],dtype=np.longdouble)

benign = y_train == 0
malignant = y_train == 1

# plot benign (blue circle)
plt.scatter(x_train[benign], y_train[benign],
            color='blue', marker='o', s=150, label='benign')

# plot malignant (red X)
plt.scatter(x_train[malignant], y_train[malignant],
            color='red', marker='x', s=150, label='malignant')

plt.xlabel("Tumor Size")
plt.ylabel("y")
plt.title("Example of Logistic Regression on Categorical Data")

plt.legend()
plt.show()