import numpy as np
import matplotlib.pyplot as plt

print "pyplot depends upon python-tk"

points=np.arange(-4,4,0.01) # 640 points
xs,ys=np.meshgrid(points,points)

z = np.sqrt(xs ** 2 + ys ** 2)
#print z

plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()
