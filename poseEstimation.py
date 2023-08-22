import freenect
import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time

def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

model_path = '/absolute/path/to/gesture_recognizer.task'
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode










base_options = BaseOptions(model_asset_path=model_path)

while True:
        
    frame = get_video()
    cv2.imshow('RGB image',frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


    
cv2.destroyAllWindows()


