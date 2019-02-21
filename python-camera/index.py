
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

def show_raw_feed(img):
    cv2.imshow('camera', img)

def convert_from_rgb_to_gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayscale', gray)
    return gray

def convert_from_rgb_to_hsv(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)
    return hsv

def mask_by_color_range(range_lower, range_upper, img):
    hsv = convert_from_rgb_to_hsv(img)
    mask = cv2.inRange(hsv, range_lower, range_upper)
    cv2.imshow('mask', mask)
    masked_result = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('masked', masked_result)

def plot_thresholds(img):
    img_blur = cv2.medianBlur(img,5).astype('uint8')
    ret, th1 = cv2.threshold(img_blur, 127, 255, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY, 11, 2)
    th3 = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY, 11, 2)
    titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img_blur, th1, th2, th3]
    for i in range(4):
        plt.subplot(2, 2, i+1),plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

def resize(img):
    res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('resized', res)

def translate(matrix, img):
    rows, cols, _ = img.shape
    M = np.float32(matrix)
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('translate static', dst)

def translate_by_angle(angle, img):
    rows, cols, _ = img.shape
    translate_x = 100 * math.cos(angle / math.pi)
    translate_y = 100 * math.sin(angle / math.pi)
    matrix = [[1,0,translate_x], [0,1,translate_y]]
    M = np.float32(matrix)
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('translate dynamic', dst)

def open_transform(img):
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow('opening', opening)

def image_gradients(img):
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F, 0, 1, ksize=5)
    plt.subplot(2, 2, 1), plt.imshow(img, cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(sobely, cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.show()

def canny_edges(img):
    edges = cv2.Canny(img,100,200)

    plt.subplot(121), plt.imshow(img, cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

def contours(img):
    
    # red color boundaries (R,B and G)
    lower = [1, 0, 20]
    upper = [60, 40, 200]

    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask=mask)

    ret,thresh = cv2.threshold(mask, 40, 255, 0)
    image, contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) != 0:
        ctr = np.array(contours).reshape((-1, 1, 2)).astype(np.int32)
        cv2.drawContours(output, ctr, -1, 255, 3)
        c = max(ctr, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow('contours', np.hstack([img, output]))

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    i = 0.5
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
        show_raw_feed(img)

        #convert_from_rgb_to_gray(img)

        #convert_from_rgb_to_hsv(img)

        #lower = np.array([0,0,0])
        #upper = np.array([80,80,80])
        #mask_by_color_range(lower, upper, img)

        #resize(img)

        #translate([[1,0,100], [0,1,50]], img)
        
        #translate_by_angle(i, img)

        #open_transform(img)

        #image_gradients(img)

        #canny_edges(img)

        contours(img)
        i += 0.25
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()