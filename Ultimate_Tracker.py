from http.client import BadStatusLine
from lib2to3.fixes.fix_set_literal import FixSetLiteral
from ssl import SSL_ERROR_WANT_X509_LOOKUP
import time
import openvr
import csv
import math
import numpy as np
from win_precise_time import sleep
import matplotlib.pyplot as plt
from collections import deque
from mpl_toolkits.mplot3d import Axes3D

a = 1
b = 2

FSL_Left  = 0 # Front Shoe Length, Left
FSL_Right = 0 # Front Shoe Length, Right
BSL_Left  = 0 # Back Shoe Length, Left
BSL_Right = 0 # Back Shoe Length, Right
SWL = 0       # Shoes Width, Largest
SWM = 0       # Shoes Width, Middle
SWH = 0       # Shoes Width, Heel


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
