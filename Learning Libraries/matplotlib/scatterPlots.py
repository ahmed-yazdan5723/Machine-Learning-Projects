import matplotlib.pyplot as plt
import numpy as np

#Datasets
x1 = np.array([0, 1, 1, 2, 4, 5, 6, 7, 7, 8]) #Hours studied
y1 = np.array([55, 60, 63, 62, 69, 70, 74, 78, 82, 86]) #Grades
x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8]) #Hours studied
y2 = np.array([55, 63, 78, 50, 49, 70, 74, 70, 82, 86, 91]) #Grades


plt.scatter(x1, y1,
            color="blue",
            alpha = 1,
            s = 100,
            label="Class A"
            )

plt.scatter(x2, y2,
            color="red",
            alpha = 1,
            s = 100,
            label="Class B"
            )

plt.xlabel("Hours studied")
plt.ylabel("Marks")

plt.legend()

#Connecting the scatter plots with lines using plt.plot() function
plt.plot(x1, y1, color='skyblue', linestyle='-', label='Connected Line')
plt.plot(x2, y2, color='pink', linestyle='-', label='Connected Line')

plt.show()