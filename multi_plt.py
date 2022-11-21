import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi,np.pi,15)

C = np.cos(X)

S = np.sin(X)

ax = plt.axes([0.1,0.1,0.8,0.8])

ax1 = ax.plot(X,C,'mx:')

ax2 = ax.plot(X,S,'cD-')

ax.legend(labels = ('Cosine function', 'Sine Function'),loc = 'upper left')

ax.set_title("Trignometric Functions in Mathematics")

plt.show()
