import sys
import numpy as np
import random
import matplotlib
import glob
import cv2 as cv
from PIL import Image
from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import DepthMap as dpm
matplotlib.use('Qt5Agg')


imgL_list = []
imgR_list = []
maps = []
bound_rect = []

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width,height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('MainWindow.ui', self)
        self.title = "Pedestrian detecting"
        self.setWindowTitle(self.title)
        self.start_stop_pushButton.clicked.connect(self.play_pushed)

        dpm.getObj()

        self.isDraw = True
        self.isPlaying = False
        self.show()
        self.current_img = 0
        self.fps = 14
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        #self.update()
        #self.play_pushed()


    def play_pushed(self):
        if self.isPlaying:
            self.stop()
            self.start_stop_pushButton.setText('START')
            self.isPLaying = False
        else:
            self.start()
            self.start_stop_pushButton.setText('STOP')
            self.isPLaying = True


    def draw(self, img, disp, ):
        pass


    def update(self):
        if self.current_img+1 >= len(imgL_list)-2:
            self.current_img = 0

        #self.current_img = 305
        pixmapL = cv.imread(imgL_list[self.current_img], cv.CV_8UC1)
        #pixmapR = cv.imread(imgR_list[self.current_img], cv.CV_8UC1)
        pixmapR = cv.imread(imgL_list[self.current_img+1], cv.CV_8UC1)

        map = cv.imread(maps[self.current_img])


        pixmap = dpm.getDepthmap(pixmapL, pixmapR)

        # if self.isDraw:
        #     self.draw()

        cv.imshow('disp', pixmap)
        cv.imshow('Main', pixmapL)
        #pix = QtGui.QImage(pixmap.data, pixmap.shape[1], pixmap.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        #self.pic_label.setPixmap(QPixmap.fromImage(pix))
        print(f'{self.current_img}')
        self.current_img += 1



    def start(self):
        self.timer.setInterval(int(1000/self.fps))
        self.timer.start()

    def stop(self):
        self.timer.stop()





def PhotoBank():
    global imgL_list
    global imgR_list
    global maps
    pathL = 'E:\Study\Pedestrian detecting\Pedestrian-detecting\DataSet\lp-left\*'#"E:/Study/Pedestrian detecting/DataSet/lp-left/*"
    pathR = 'E:/Study/Pedestrian detecting/Pedestrian-detecting/DataSet/lp-right/*'#"E:/Study/Pedestrian detecting/DataSet/lp-right/*"
    mapPath = 'E:\Study\Pedestrian detecting\Pedestrian-detecting\DataSet\maps-loewenplatz\maps-sfm-avg-jan2010\*'
    bound_rect_path = 'E:\Study\Pedestrian detecting\Pedestrian-detecting\DataSet\lp-annot.idl'
    bound = glob.glob(bound_rect_path)

    with open(bound_rect_path, 'r') as f:
        f.read().splitlines()
    print(f)
    # for filename in glob.glob(pathL):  # assuming gif
    #     im = Image.open(filename)
    #     imgL_list.append(im)
    imgL_list = glob.glob(pathL)
    imgR_list = glob.glob(pathR)
    maps = glob.glob(mapPath)


def main():
    PhotoBank()
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
