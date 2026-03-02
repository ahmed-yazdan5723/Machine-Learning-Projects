import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
np.set_printoptions(precision=2)

X_train, y_train = load_house_data()
X_features = ['size(sqft)','bedrooms','floors','age']
