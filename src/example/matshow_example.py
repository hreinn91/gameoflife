import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# a 2D array with linearly increasing values on the diagonal
matplotlib.pyplot.style.use('dracula')
a = np.diag(range(15))

plt.matshow(a)

plt.show()
