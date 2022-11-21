import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,400)

y = np.sin(x**2)+np.cos(x)

fig,ax = plt.subplots()

ax.plot(x,y)

ax.set_title('Simplest plot in the matplotlib')
