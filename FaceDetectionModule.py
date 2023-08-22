import freenect
import cv2
import numpy as np
import mediapipe as mp
import time

class FaceDetector:
    def __init__(self):
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceDetection = self.mpFaceDetection.FaceDetection()
        self.pTime = 0

    def get_video(self):
        array, _ = freenect.sync_get_video()
        array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
        return array

    def run(self):
        while True:
            frame = self.get_video()

            cTime = time.time()
            fps = 1 / (cTime - self.pTime)
            self.pTime = cTime
            cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
            results = self.mpFaceDetection.process(frame)
            print(results)

            if results.detections:
                for id, detection in enumerate(results.detections):
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, ic = frame.shape
                    bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                            int(bboxC.width * iw), int(bboxC.height * ih)
                    cv2.rectangle(frame, bbox, (255, 0, 255), 2)
                    cv2.putText(frame, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20),
                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

            cv2.imshow('RGB image', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # cv2.destroyAllWindows()


if __name__ == '__main__':
    faceDetector = FaceDetector()
    faceDetector.run()
