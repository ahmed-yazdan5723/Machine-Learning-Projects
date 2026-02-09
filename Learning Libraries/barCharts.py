import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4,3,2,5,3,1])

plt.bar(categories, values, color="skyblue")
# plt.barh(categories, values, color="skyblue")

plt.title("Daily Food Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")








plt.show()