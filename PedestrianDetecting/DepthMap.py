import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt



imgL = cv.imread("E:\Study\Pedestrian detecting\Pedestrian-detecting\DataSet\lp-left\image_00005205_0.png", 0)
imgR = cv.imread("E:\Study\Pedestrian detecting\Pedestrian-detecting\DataSet\lp-left\image_00005206_0.png", 0)
obj_path = 'E:\Study\Pedestrian detecting\Pedestrian-detecting\DataSet\maps-loewenplatz\maps-sfm-avg-jan2010\path.txt'
K1 = np.array([[801.25700, 0., 325.05589], [0.,  802.24324, 243.29150], [0., 0., 1.]])
K2 = np.array([[804.81163, 0., 335.67663], [0.,  805.19672, 232.42614], [0., 0., 1.]])
rad1 = np.array([-0.22813,   0.16483])
rad2 = np.array([-0.21484,   0.10025])
dist1 = np.array([-0.22813,   0.16483,  0., 0.])
dist2 = np.array([-0.21484,   0.10025,  0., 0.])

Rt1 = np.array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
Rt2 = np.array([[0.999923235343999,  -0.005513666805298,   0.011096075772572],
       [ 0.005431036122504,   0.999957401012593,   0.007463243716854],
       [-0.011136752930121,  -0.007402407615178,  0.999910584550275]])

C1 = np.array([0., 0., 0.])
C2 = np.array([-0.6192593383286313, -0.0007428029644263, -0.0142760640908179])
obj_pnt = []


def getObj():
    f = open(obj_path, 'r', )
    for line in f:

        obj_pnt.append(line.strip().split(sep=' '))
    f.close()
    for line in obj_pnt:
        for i in range(len(line)):
            line[i] = float(line[i])


#imgL = cv.cvtColor(imgL, imgL,  cv.COLOR_BGR2RGB)
def getDepthmap(imgL, imgR):
    # obj_pnts = np.array(obj_pnt)
    # #left calib
    # hl, wl = imgL.shape[:2]
    # new_mtxL, roiL = cv.getOptimalNewCameraMatrix(K1, dist1, (wl, hl),1,(wl,hl))
    # #imageL = new_mtxL#imgL
    #
    # #right calib
    # hr, wr = imgR.shape[:2]
    # new_mtxR, roiR = cv.getOptimalNewCameraMatrix(K2, dist2, (wr, hr), 1, (wr, hr))
    # #imageR = new_mtxR#imgR
    #
    # flags = 0
    # flags |= cv.CALIB_FIX_INTRINSIC
    # # Here we fix the intrinsic camara matrixes so that only Rot, Trns, Emat and Fmat are calculated.
    # # Hence intrinsic parameters are the same
    #
    #
    # criteria_stereo = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # retS, new_mtxL, distL, new_mtxR, distR, Rot, Trns, Emat, Fmat = cv.stereoCalibrate(obj_pnts, imgL, imgR,
    #                                                                                    new_mtxL, dist1, new_mtxR,
    #                                                                                    dist2, imgL.shape[::-1],
    #                                                                                    criteria_stereo, flags)
    #
    # rectify_scale = 1
    # rect_l, rect_r, proj_mat_l, proj_mat_r, Q, roiL, roiR = cv.stereoRectify(new_mtxL, dist1, new_mtxR, dist2,
    #                                                                           imgL.shape[::-1], Rot, Trns,
    #                                                                           rectify_scale, (0, 0))
    #
    # #Пропарсить файлы и вытащить от туда значения
    # imageL = cv.initUndistortRectifyMap(new_mtxL, distL, rect_l, proj_mat_l, imgL.shape[::-1], cv.CV_8UC1)
    # imageR = cv.initUndistortRectifyMap(new_mtxR, distR, rect_l, proj_mat_r, imgR.shape[::-1], cv.CV_8UC1)
    imageL = imgL
    imageR = imgR

    stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(imageL, imageR)
    return disparity/255




def imgCVshow(disparity):
    plt.imshow(disparity, 'gray')
    cv.imshow('Left', imgL)
    cv.imshow('Right', imgR)
    plt.show()
    cv.waitKey()

def main():
    imgCVshow(getDepthmap(imgL, imgR))

if __name__ == '__main__':
    main()
