import cv3
import numpy as np
import matplotlib.pyplot as plt

img = cv3.imread('xyz.jpg', cv3.IMREAD_UNCHANGED)

#IMREAD_GREYSCALE = 0
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

cv3.imshow('Image', img)
cv3.waitkey(0)
cv3.destroyAllWindows()

#also for showing image we can use
#plt.imshow(img, cmap ='gray', interpolation = 'bicubic')
#plt.show()

#cv3.imwrite('xyzg.png',img)


