# Importing libraries
import matplotlib.pyplot as plt
import numpy as np

# Datasets
x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 3])
y2 = np.array([17, 33, 67, 4])
y3 = np.array([1, 5, 9, 7])

# Creating a dictionary for customizing plt
line_style = dict(
         marker="o", 
         ms=10, 
         mfc="#ff0000",
         mec="#000000", 
         linestyle="solid", 
         linewidth=2,
        #  color="cyan",
        )

# Labeling the graphs
plt.title("Class size", 
          fontsize=25, 
          family="Arial", 
          fontweight="bold", 
          color="#000000"
        )
plt.xlabel("Year", fontsize=20,family="Arial", 
          fontweight="bold", 
          color="#000000")
plt.ylabel("Students", fontsize=20,family="Arial", 
          fontweight="bold", 
          color="#000000")

# Customizing the ticks
plt.tick_params(axis="both",
                colors="black")


# Plotting the datasets in plt
# plt.plot(x,y1, color="#0000FF", **line_style)
# plt.plot(x,y2, color="#124F06", **line_style)
# plt.plot(x,y3, color="#7B2377", **line_style)

# Changing the increment of values in axis
plt.xticks(x)

# GRID
xg = np.array([1,2,3,4,5])
yg = np.array([5,3,9,7,27])

plt.grid(axis="y", linewidth=1.5, linestyle="dashed")

plt.plot(xg,yg, **line_style)



# Showing the plots
plt.show()