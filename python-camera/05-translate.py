from cam import stream
from window import show_horizontal_stack_images
import cv2
import numpy as np
import math

# matrix for static translation
matrix = [[1,0,100], [0,1,50]]
angle = 0.00
angle_step = 0.25

def translate_static(matrix, img):
    rows, cols, _ = img.shape
    M = np.float32(matrix)
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst

def translate_by_angle(angle, img):
    rows, cols, _ = img.shape
    translate_x = 100 * math.cos(angle / math.pi)
    translate_y = 100 * math.sin(angle / math.pi)
    matrix = [[1,0,translate_x], [0,1,translate_y]]
    M = np.float32(matrix)
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst


def translate(img):
    global matrix, angle, angle_step
    # translate input image by matrix defined at top of file
    static_translation = translate_static(matrix, img)
    
    # increment angle for angle-based translation
    angle += angle_step

    # translate input image dynamically by incrementing angle
    angle_based_translation = translate_by_angle(angle, img)

    #show window
    show_horizontal_stack_images('RGB -> Static Translation -> Angle-based Translation ', [img, static_translation, angle_based_translation])

stream(translate)
