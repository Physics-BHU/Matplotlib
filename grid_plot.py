import matplotlib.pyplot as plt

def annotate_axes(fig):
  for i, ax in enumerate(fig.axes):
    ax.text(0.5,0.5,"block%d"%(i+1),va = "center",ha="center")

    ax.tick_params(labelbottom = False, labelleft = False)

ax1 = plt.subplot2grid((3,3),(0,0),colspan = 3)

ax2 = plt.subplot2grid((3,3),(1,0),colspan = 2)

ax3 = plt.subplot2grid((3,3),(1,2),colspan = 2)

ax4 = plt.subplot2grid((3,3),(2,0))

ax5 = plt.subplot2grid((3,3),(2,1))

annotate_axes(fig)

matplotlib.pyplot.grid()

plt.show()
