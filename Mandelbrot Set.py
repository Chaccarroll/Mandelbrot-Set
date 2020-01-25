import numpy as np
import matplotlib.pyplot as plt
from numba import jit

#we use jit to speed up the time it takes to run the code
@jit
def mandelbrot(re, im, max_iter):  #re and im stand for real and imaginary. max_iter stand for the maximum iterations.
    c = complex(re, im)
    z = 0.0j
    for i in range (max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return max_iter

#these handle the resolution
columns = 2000
rows = 2000


result = np.zeros([rows, columns])
for row_index, re in enumerate(np.linspace(-2,1,num=rows)):
    for column_index, im in enumerate(np.linspace(-1,1,num=columns)):
        result[row_index, column_index] = mandelbrot(re, im, 100)


#We use matplotlib.pyplot to plot the set
plt.figure(dpi = 100)  #sets it to 100 pixles
plt.imshow(result.T, cmap = "hot", interpolation = "bilinear", extent = [-2,1,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()

