

import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0,2*np.pi,400)

y = np.sin(x**2)

plt.plot(x,y,'orange')

plt.title("Customized Plots")

#Customize grids

plt.grid(True,color = "black", linewidth = "1.4",linestyle = "-.")

plt.show()
