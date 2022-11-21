y = np.random.rand(3, 4)

plt.bar(x + 0.00, y[0], color = 'b', width = 0.25)

plt.bar(x + 0.25, y[1], color = 'g', width = 0.25)

plt.bar(x + 0.50, y[2], color = 'r', width = 0.25)

plt.show()
