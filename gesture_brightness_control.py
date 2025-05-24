import cv2
import mediapipe as mp
import numpy as np
import time 
import hand_tracking_module as htm
import math
import screen_brightness_control as sbc

wcam, hcam = 640 , 480

cap = cv2.VideoCapture(0)

cap.set(3,wcam)
cap.set(4,hcam)

prevT = 0

current_brightness = sbc.get_brightness()
print(current_brightness)

minBright = 0
maxBright = 100
bright = 0
brightBar = 400

detector = htm.handDetector(detconf=0.5)
while True :
    ret, img = cap.read()
    img = detector.handdetect(img)
    lmlist = detector.findpos(img,draw=False)
    if len(lmlist) :
        # print(lmlist[4],lmlist[8])

        # thumb tip
        x1,y1 = lmlist[4][1],lmlist[4][2]
        cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)

        # index finger tip
        x2,y2 = lmlist[8][1],lmlist[8][2]
        cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)

        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)

        cx,cy = (x1+x2)//2 , (y1+y2)//2
        cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

        length = math.hypot(x2-x1,y2-y1)
        # print(length)

        # hand range -> 50 to 270
        # bright range -> 0 to 100

        bright = np.interp(length,(50,270),(minBright,maxBright))
        brightBar = np.interp(length,(50,270),(400,150))
        sbc.set_brightness(bright)

        if length < 50:
            cv2.circle(img,(cx,cy),15,(255,255,255),cv2.FILLED)

    cv2.rectangle(img,(60,150),(85,400),(238,130,238),3)
    cv2.rectangle(img,(60,int(brightBar)),(85,400),(238,130,238),cv2.FILLED)

    currT = time.time()
    fps = 1/(currT-prevT)
    prevT = currT
    cv2.putText(img,str(int(fps)) + ' FPS',(40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),3)
    cv2.putText(img,f'Brightness : {int(bright)} %',(40,450), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),3)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break