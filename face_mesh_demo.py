import cv2
import mediapipe as mp
import time
import freenect
import numpy as np

def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)

while True:
    frame = get_video()
    results = faceMesh.process(frame)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(frame,faceLms,mpFaceMesh.FACEMESH_CONTOURS)
            for id,lm in enumerate(faceLms.landmark):
                #print(lm)
                ih,iw,ic = frame.shape
                x,y = int(lm.x*iw),int(lm.y*ih)
                print(id,x,y)

        






    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


    cv2.imshow('RBG IMAGE', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


    
cv2.destroyAllWindows()

