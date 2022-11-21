fig = plt.figure()

ax = plt.axes(projection= '3d')

ax.plot_surface(X, Y, Z, color = 'Blue')

ax.set_title('Surface Plot')

plt.show()
