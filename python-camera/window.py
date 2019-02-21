import cv2
import numpy as np

def show_horizontal_stack_images(title, images):
    cv2.imshow(title, np.hstack(images))