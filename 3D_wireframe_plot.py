fig = plt.figure()

ax = plt.axes(projection = '3d')

ax.plot_wireframe(X,Y, Z, color = 'Green')

ax.set_title('wireframe')

plt.show()
