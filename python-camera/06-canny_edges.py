from cam import stream
from window import show_horizontal_stack_images
import cv2

def canny_edges(img):
    # find edges
    edges = cv2.Canny(img,100,200)
    
    # convert back to 3 channel to enable horizontal stacking
    edges_3_channel = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    show_horizontal_stack_images('RGB -> Canny Edges ', [img, edges_3_channel])

stream(canny_edges)