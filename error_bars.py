x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

ye = np.random.rand(len(x))/10
plt.errorbar(x,y,yerr=ye)
plt.show()
