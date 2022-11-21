import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(0,math.pi*2,0.05)
y = np.cos(x)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_title("Cos Wave") #used to set the title
ax.set_xlabel('angle')  #used to set label for x-axis
ax.set_ylabel('cos') #used to set label for y-axis
plt.figure()

fig.add_axes([0,0,1,1])
print(type(fig))
