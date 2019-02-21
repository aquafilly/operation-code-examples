from cam import stream
from window import show_horizontal_stack_images
import cv2

def convert_from_rgb_to_hsv(img):
    #convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #show window
    show_horizontal_stack_images('RGB -> HSV', [img, hsv])

stream(convert_from_rgb_to_hsv)
