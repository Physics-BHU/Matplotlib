x = np.linspace(-10, 10, 30)

y = np.linspace(-10, 10, 30)

X, Y = np.meshgrid(x, y)

Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure()

ax = fig.add_subplot(projection = '3d')

ax.contour(X, Y, Z, 50, cmap = 'coolwarm')

plt.show()
