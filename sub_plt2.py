import matplotlib.gridspec as gridspec

fig = plt.figure(constrained_layout = True)
specs = gridspec.GridSpec(ncols = 2, nrows = 2, figure = fig)
ax1 = fig.add_subplot(specs[0,0])

ax2 = fig.add_subplot(specs[0,1])


ax3 = fig.add_subplot(specs[1,0])


ax4 = fig.add_subplot(specs[1,1])

plt.show()
