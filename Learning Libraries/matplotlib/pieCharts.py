import numpy as np
import matplotlib.pyplot as plt

categories = np.array(["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4,3,2,5,3,1])
colors = np.array(["khaki", "orange", "green", "gray", "#F8F0E3", "pink"])
m = values.shape[0]
print(m)
plt.pie(values, 
        labels=categories,
        autopct="%1.2f%%",
        colors=colors,
        explode=[0,0,0,0,0,0.1],
        # shadow=True
        # startangle=180
        )
plt.title("Food Consumption Pie Chart")
plt.show()

# colors="skyblue, red, green, blue, orange, pink"