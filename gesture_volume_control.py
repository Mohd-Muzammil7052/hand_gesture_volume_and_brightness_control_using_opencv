import cv2
import mediapipe as mp
import numpy as np
import time 
import hand_tracking_module as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wcam, hcam = 640 , 480

cap = cv2.VideoCapture(0)

cap.set(3,wcam)
cap.set(4,hcam)

prevT = 0

device = AudioUtilities.GetSpeakers()
interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface,POINTER(IAudioEndpointVolume))
# print(f"Audio output: {device.FriendlyName}")
# print(f"- Muted: {bool(volume.GetMute())}")
# print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB")
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0

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
        # vol range -> -63.5 to 0

        vol = np.interp(length,(50,270),(minVol,maxVol))
        volBar = np.interp(length,(50,270),(400,150))
        volPer = np.interp(length,(50,270),(0,100))
        # print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img,(cx,cy),15,(255,255,255),cv2.FILLED)

    cv2.rectangle(img,(60,150),(85,400),(238,130,238),3)
    cv2.rectangle(img,(60,int(volBar)),(85,400),(238,130,238),cv2.FILLED)

    currT = time.time()
    fps = 1/(currT-prevT)
    prevT = currT
    cv2.putText(img,str(int(fps)) + ' FPS',(40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),3)
    cv2.putText(img,f'Volume : {int(volPer)} %',(40,450), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),3)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break