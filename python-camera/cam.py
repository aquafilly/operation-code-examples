import cv2

def stream(image_handler):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
        if image_handler:
            image_handler(img)