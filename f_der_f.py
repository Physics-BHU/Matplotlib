import numpy as np

import matplotlib.pyplot as plt

plt.figure(figsize = (6,4))

def f(x):
  return np.sin(x) - x*np.cos(x)

def fp(x):
  """The derivative fucntion of f"""
  return x*np.sin(x)

X = np.arange(-5,5.0,0.05)

fig, ax = plt.subplots(2,sharex = 'col',sharey = 'row')

ax[0].plot(X,f(X),'bo',X,f(X),'k')
ax[0].set(title = 'The function f')

ax[1].plot(X,fp(X),'go',X,fp(X),'k')
ax[1].set(xlabel='X values',ylabel = 'Y Values', title = 'Derivative Function of f')

plt.show()
