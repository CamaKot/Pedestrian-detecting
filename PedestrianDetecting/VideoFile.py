import numpy
import cv2 as cv



file = "E:\Study\Pedestrian detecting\DataSet\loewenplatz.avi"
cap = cv.VideoCapture(file)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()