import freenect
import cv2
import numpy as np
import mediapipe as mp
import time

def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
mpFaceDetection = mpFaceDetection.FaceDetection()


















while True:
    frame = get_video()
    
    cTime = time.time() 
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    results = mpFaceDetection.process(frame)
    print(results)

    if results.detections:
        for id,detection in enumerate(results.detections):
            #mpDraw.draw_detection(frame,detection)
            #print(id,detection)
            #print(detection.score)
            #print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            ih,iw,ic = frame.shape
            bbox = int(bboxC.xmin*iw),int(bboxC.ymin*ih),\
                   int(bboxC.width*iw),int(bboxC.height*ih)
            cv2.rectangle(frame,bbox,(255,0,255),2)
            cv2.putText(frame,f'{int(detection.score[0]*100)}%',(bbox[0],bbox[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)


    cv2.imshow('RGB image',frame)
    cv2.waitKey(1) 


cv2.destroyAllWindows()


