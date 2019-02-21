from cam import stream
from window import show_horizontal_stack_images
import cv2

def convert_from_rgb_to_gray(img):
    #convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #convert back to 3 channel to enable horizontal stacking
    gray_3_channel = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    #show window
    show_horizontal_stack_images('RGB -> GRAY', [img, gray_3_channel])

stream(convert_from_rgb_to_gray)
