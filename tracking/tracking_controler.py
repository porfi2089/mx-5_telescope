import cv2 as cv
import numpy as np
import time


input_video = cv.VideoCapture(0)
input_video.set(cv.CAP_PROP_FRAME_WIDTH, 640)
input_video.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = input_video.read()
    if not ret:
        break

    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

