# -*- coding: utf-8 -*-
"""pie_chart_plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QrbPwOGcHI5dckhpgc3mkuL650FUZqBK
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

data = np.array([35,25,25,15])

plt.pie(data)

plt.show()

mylabels = ['A','B','C','D']
plt.pie(data, labels = mylabels)

plt.show()

explode = [0.0, 0.05, 0.1, 0.15]

plt.pie(data, labels = mylabels, explode = explode)

plt.show()

plt.pie(data, labels = mylabels, explode = explode, shadow = True)

plt.show()

plt.pie(data, labels = mylabels, explode = explode, shadow = True)

plt.legend()

plt.show()

plt.pie(data, labels = mylabels, explode = explode, shadow = True)

plt.legend(title = 'Data : ')

plt.show()

N = 20

theta = np.linspace(0.0, 2*np.pi, N)

r = 10*np.random.rand(N)

plt.subplot(projection = 'polar')

plt.bar(theta, r, bottom = 0.0, color = ['r','g','b'], alpha = 0.2)

plt.show()

r = np.arange(0, 5, 0.2)

theta = 2*np.pi*r

plt.subplot(projection = 'polar')

plt.plot(theta, r)

plt.show()

r = np.arange(0, 5, 0.01)

theta = 2*np.pi*r

plt.subplot(projection = 'polar')

plt.plot(theta, r)

plt.show()

N = 150

r = np.random.rand(N)

theta = 2*np.pi*np.random.rand(N)

size = r * 100

plt.subplot(projection = 'polar')

plt.scatter(theta, r, c = theta, s = size, cmap = 'hsv', alpha = 0.5)

plt.show()

fig = plt.figure()

ax = fig.add_subplot(projection = 'polar')

c = ax.scatter(theta, r, c = theta, s = size, cmap = 'hsv', alpha = 0.5)

ax.set_thetamin(0)

ax.set_thetamax(90)

plt.show()

