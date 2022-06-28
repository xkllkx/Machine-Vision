import cv2
import mediapipe as mp
import time
import numpy as np
from numpy import array, uint8

def get_red(img):
    redImg = img[:,:,2]
    return redImg

def get_green(img):
    greenImg = img[:,:,1]
    return greenImg

def get_blue(img):
    blueImg = img[:,:,0]
    return blueImg

def findcontour(img: np.ndarray):
    cv2.threshold(img, dst=img, *(140, 255, 0))
    cv2.morphologyEx(img, dst=img, *(2, array([[0, 1, 0],
                                               [1, 1, 1],
                                               [0, 1, 0]], dtype=uint8)), iterations=1)
    kernel = np.ones((2, 2), np.uint8)
    for i in range (100):
        #cv2.dilate(img, kernel=kernel)
        cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    
    
    

    '''
    cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) 
    
    for i in range (10):
        cv2.dilate(img, kernel=kernel)                                           
    
    cv2.erode(img, dst=img, *(array([[1, 1],
                                     [1, 1]], dtype=uint8),), iterations=1)
   
    cv2.morphologyEx(img, dst=img, *(2, array([[0, 1, 1, 0],
                                               [1, 0, 0, 1],
                                               [1, 0, 0, 1],
                                               [0, 1, 1, 0]], dtype=uint8)), iterations=1)

    cv2.morphologyEx(img, dst=img, *(2, array([[1, 1, 1, 1, 1, 1, 1],
                                               [1, 0, 0, 0, 0, 0, 1],
                                               [1, 0, 0, 0, 0, 0, 1],
                                               [1, 0, 0, 0, 0, 0, 1],
                                               [1, 0, 0, 0, 0, 0, 1],
                                               [1, 0, 0, 0, 0, 0, 1],
                                               [1, 1, 1, 1, 1, 1, 1]], dtype=uint8)), iterations=1)

    cv2.morphologyEx(img, dst=img, *(2, array([[0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 1, 0, 1, 0, 0],
                                               [0, 1, 0, 0, 0, 1, 0],
                                               [1, 0, 0, 0, 0, 0, 1],
                                               [0, 1, 0, 0, 0, 1, 0],
                                               [0, 0, 1, 0, 1, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0]], dtype=uint8)), iterations=1)
    
    for i in range (10):
        #cv2.erode(img, kernel=kernel)
        cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    '''
    '''
    
    cv2.morphologyEx(img, dst=img, *(2, array([[0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [1, 1, 1, 1, 1, 1, 1],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0]], dtype=uint8)), iterations=1)
    
    cv2.erode(img, dst=img, *(array([[0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0],
                                     [1, 1, 1, 1, 1],
                                     [0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0]], dtype=uint8),), iterations=1)

    cv2.dilate(img, dst=img, *(array([[0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [1, 1, 1, 1, 1, 1, 1],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0]], dtype=uint8),), **{'iterations': 8})
    '''
    return img


if __name__ == '__main__':

    img = cv2.imread("image2.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = get_red(img)

    img = findcontour(img_gray)
    
    '''
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_copy = img_gray.copy()
    process = findcontour(img_gray)
    process = cv2.Canny(process, 200, 255, apertureSize=5)
    if "3.0" < cv2.__version__ < "3.5":
        _, cnts, hierarchy = cv2.findContours(process, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    else:
        cnts, hierarchy = cv2.findContours(process, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)

    for c in cnts:
        if cv2.contourArea(c) < 300:
            continue
        M = cv2.moments(c)
        Cx = int(M["m10"] / M["m00"])
        Cy = int(M["m01"] / M["m00"])
        cv2.circle(img, (Cx, Cy), 10, (1, 227, 254), -1)
    '''
    #cv2.imwrite("tt.jpg", img)
    cv2.namedWindow("image2", cv2.WINDOW_NORMAL)
    #cv2.namedWindow("compare", cv2.WINDOW_NORMAL)
    cv2.imshow("image2", img)
    #cv2.imshow("compare", img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()