fig = plt.figure()

ax = plt.axes(projection = '3d')

z = np.linspace(0,30,1000)

x = np.sin(z)

y = np.cos(z)

ax.plot3D(x,y,z,'red')

plt.show
