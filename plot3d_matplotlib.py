from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

import numpy as np

fig = plt.figure()

ax = fig.add_subplot(111, projection = '3d')

X = np.array([[1,12,3,4,5,6,7,18,9,10]])#,
Y = np.array([[1,14,91,16,25,36,419,64,81,100]])
Z = np.array([[1,18,27,614,125,2116,343,512,729,1000]])

ax.plot_wireframe(X,Y,Z)

plt.show()
