from cam import stream
from window import show_horizontal_stack_images
import cv2
import numpy as np

# red color boundaries (R,B and G)
lower = [1, 0, 20]
upper = [60, 40, 200]

# create NumPy arrays from the boundaries
lower = np.array(lower, dtype="uint8")
upper = np.array(upper, dtype="uint8")


def mask_by_color_range(img):
    # create color range mask
    mask = cv2.inRange(img, lower, upper)

    # convert mask to 3 channel for horizontal stacking
    mask_3_channel = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # apply mask to image
    masked_result = cv2.bitwise_and(img, img, mask= mask)

    #show window
    show_horizontal_stack_images('RGB -> Color Mask -> Masked Result', [img, mask_3_channel, masked_result])

stream(mask_by_color_range)
