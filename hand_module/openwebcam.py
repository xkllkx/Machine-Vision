import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
import time

cap = cv2.VideoCapture(0) #設定攝像頭做影片擷取

while True:
    success, img = cap.read()
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()