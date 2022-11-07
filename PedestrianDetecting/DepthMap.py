import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgL = cv.imread("images/image_00005125_0.png", 0)
imgR = cv.imread("images/image_00005126_0.png", 0)

#imgL = cv.cvtColor(imgL, imgL,  cv.COLOR_BGR2RGB)

stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL, imgR)
plt.imshow(disparity, 'gray')
plt.show()