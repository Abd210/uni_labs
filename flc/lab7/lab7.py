import numpy as np
import matplotlib.pyplot as plt

# Ex 1
ex1 = [1.4, 5.9, 2.6, 7.3, 8.5, 9.3, 6.1]
array1 = np.array(ex1)
print("Exercise 1 - Converted list to array:", array1)

# Ex 2
ex2 = np.arange(70, 92, 2)  # 92 is exclusive, so it includes up to 90
print("Exercise 2 - 1D array of even numbers between 70 and 91:", ex2)

# Ex 3
ex3 = np.zeros((3, 3), dtype=int)
np.fill_diagonal(ex3, [3, 7, 11])
print("Exercise 3 - 3x3 matrix with 3, 7, 11 on the main diagonal:\n", ex3)

# Ex 4
ex4 = np.arange(10, 16).reshape((2, 3))
print("Exercise 4 - 2x3 array of numbers between 10 and 16:\n", ex4)

# Ex 5
ex5 = np.array([[10, 50, 70, 20, 40], [5, 45, 95, 35, 65]])
above_43 = ex5[ex5 > 43]
below_43 = ex5[ex5 < 43]
print("Ex 5 - Numbers above 43:", above_43)
print("Ex 5 - Numbers below 43:", below_43)

# Ex 6
np.savetxt("array_ex5.txt", ex5, fmt="%d")
loaded_ex5 = np.loadtxt("array_ex5.txt", dtype=int)
print("Ex 6 - Loaded array from text file:\n", loaded_ex5)


# Ex 7: Create a 3x2 subplot layout
fig, axs = plt.subplots(3, 2, figsize=(10, 12))
fig.suptitle("Ex 7 - 3x2 Subplot")

# 7.1 Line with custom marker color for points
x = np.linspace(0, 2, 10)
y = x**2
axs[0, 0].plot(x, y, marker='o', color='green', markerfacecolor='magenta')
axs[0, 0].set_title("Line with Custom Marker Color")

# 7.2 Line with custom style and grid
x = np.linspace(0, 10, 10)
y = 2 * x + 1
axs[0, 1].plot(x, y, 'g--')  # Dashed green line
axs[0, 1].grid(True)
axs[0, 1].set_title("Line with Custom Style and Grid")

# 7.3 Vertical bars with custom color, width
x = np.arange(10, 17)
y = np.random.randint(1, 20, size=len(x))
axs[1, 0].bar(x, y, color='black', width=0.5)
axs[1, 0].set_title("Vertical Bars with Custom Color and Width")

# 7.4 Scattered points with different colors
x = np.random.rand(20) * 10
y = np.random.rand(20) * 10
colors = np.random.rand(20)
sizes = 100 * np.random.rand(20)
axs[1, 1].scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
axs[1, 1].set_title("Scattered Points with Different Colors")

# 7.5 One line with custom style and color, another with custom width and color
x = np.linspace(80, 100, 10)
y1 = np.sqrt(x)
y2 = np.log(x)
axs[2, 0].plot(x, y1, 'b-.', label='Custom Style and Color')  # Blue dash-dot line
axs[2, 0].plot(x, y2, color='yellow', linewidth=4, label='Custom Width and Color')
axs[2, 0].legend()
axs[2, 0].set_title("Two Lines with Custom Styles")

# 7.6 Horizontal bars with custom color and height
y = np.arange(1, 6)
widths = np.random.randint(50, 100, size=len(y))
axs[2, 1].barh(y, widths, color='magenta', height=0.6)
axs[2, 1].set_title("Horizontal Bars with Custom Color and Height")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to fit title
plt.show()

# Ex 8: Create a plot with intersecting lines of different colors
import matplotlib.pyplot as plt
x = range(-10, 11)
y1 = [2 * i + 3 for i in x]  # Line 1: y = 2x + 3
y2 = [-0.5 * i - 2 for i in x]  # Line 2: y = -0.5x - 2

plt.plot(x, y1, color='blue', label="y = 2x + 3")
plt.plot(x, y2, color='red', label="y = -0.5x - 2")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot with Intersecting Lines of Different Colors")

plt.legend()

plt.grid()
plt.show()


# Ex 9: Create a pie chart with 5 items of custom colors and shadow
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 25, 20, 10]
colors = ['pink', 'purple', 'blue', 'green', 'red']
plt.figure()
plt.pie(sizes, labels=labels, colors=colors, shadow=True, startangle=140, autopct='%1.1f%%')
plt.title("Ex 9 - Custom Pie Chart with Shadow")
plt.show()