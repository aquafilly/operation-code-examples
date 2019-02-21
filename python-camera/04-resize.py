from cam import stream
import cv2

def resize(img):
    res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('resized', res)

stream(resize)