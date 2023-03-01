import cv2
import numpy as np
import time
import sys
sys.path.append('E:\projekty python\pose estimation')
import PoseMOdule as pm


cap = cv2.VideoCapture('curls.mp4')
detector = pm.PoseDetector()
# arm = input('Arm(L,R): ')
add = 0
# if arm == 'R':
#     add = 1
#     arm.upper()
count = 0
direction = 0

while True:
    success, img = cap.read()
    # img = cv2.imread('test.jpg')
    img = detector.findPose(img)
    lmlist = detector.findPosition(img, False)
    if len(lmlist) != 0:
        angle = detector.findAngle(img, 11+add, 13+add, 15+add)
        per = np.interp(angle, (60, 150), (100, 0))
        if per == 100:
            if direction == 0:
                count += 0.5
                direction = 1
        if per == 0:
            if direction == 1:
                count += 0.5
                direction = 0
        print(count)
        cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN,
                    2, (0, 0, 255), 2)

    cv2.imshow('Image', img)
    cv2.waitKey(1)
