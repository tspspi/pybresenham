import matplotlib.pyplot as plt
import numpy as np

from bresenham import trace_line, trace_line_antialiased_it

fig, ax = plt.subplots(1,2,figsize=(6.4, 4.8*2))

img = np.zeros((51, 21))
for pt in trace_line((-25,-10),(10,10)):
    img[int(pt[0]) + 25, int(pt[1]) + 10] = 1
ax[0].imshow(img)

imgaa = np.zeros((51, 21))
for pt, weight in trace_line_antialiased((-25,-10),(10,10)):
    imgaa[int(pt[0]) + 25, int(pt[1]) + 10] = weight
ax[1].imshow(imgaa)
