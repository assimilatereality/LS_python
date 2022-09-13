import matplotlib.pyplot as plt
plt.axes()
rectangle = plt.Rectangle((10, 10), 100, 100, fc='r', fill=False,edgecolor="r")
plt.gca().add_patch(rectangle)
plt.axis('scaled')
plt.show()