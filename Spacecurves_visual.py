from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d

# Changes the size of the aspect ratio
fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection='3d')
ax.grid()

# Range of t (start, stop, skip)
t = np.arange(0, 4*np.pi, np.pi/8)

# r(t) = f(t)i, g(t)j, h(t)k
i, j, k = np.cos(t), np.sin(t), t

ax.plot3D(i, j, k)
ax.set_title('Space Curve for r(t)')

# Distance the labels are from the axis
ax.set_xlabel('x', labelpad=25)
ax.set_ylabel('y', labelpad=25)
ax.set_zlabel('z', labelpad=25)

plt.show()

