import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = 1
b = 2

x = np.linspace(-5, 5, 100) 
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)  

z = a * x**2 + b * y**2

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5) 

ax.set_title('Elliptic Paraboloid', fontsize=15)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()
