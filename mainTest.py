import freenect
# from freenect import sync_get_depth as get_depth, sync_get_rgb as get_rgb
# from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import cv2
import numpy as np
import mediapipe as mp
import time


class handDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
    
        self.mpHands = mp.solutions.hands 
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self,img,draw=True):

        while True:
            
            frame = get_video()
            results = self.hands.process(frame)
            # print(results.multi_hand_landmarks)


            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                   if draw:
                        self.mpDraw.draw_landmarks(frame,handLms,self.mpHands.HAND_CONNECTIONS)

            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime

            cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array


def main():

    pTime = 0
    cTime = 0
    detector = handDetector()



    while True:
        
        frame = get_video()
        detector.findHands(frame)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)



    cv2.imshow('RGB image',frame)
    cv2.waitKey(1)
    
