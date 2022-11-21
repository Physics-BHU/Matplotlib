fig = plt.figure()

ax = plt.axes(projection='3d')

y = np.random.random(100)

x = np.random.random(100)

z = np.random.random(100)

ax.scatter3D(x, y, z, cmap = 'cool')

plt.show()
