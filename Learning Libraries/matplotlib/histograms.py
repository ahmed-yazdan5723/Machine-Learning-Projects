import numpy as np
import matplotlib.pyplot as plt

#Generating dataset of 100 marks students got using np.random.normal() function
scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)

plt.hist(scores, bins=10, color="pink", edgecolor = "black")

plt.title("Exam scores")
plt.xlabel("Score")
plt.ylabel("# of students")



plt.show()