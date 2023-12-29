import cv2
import apriltag

class ApriltagDetect:
    def __init__(self):
        self.target_id = 0
        self.at_detector = apriltag.Detector(apriltag.DetectorOptions(families='tag36h11'))

    def update_frame(self,frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        tags = self.at_detector.detect(gray)
        for tag in tags:
            print(tag.tag_id)
            cv2.circle(frame, tuple(tag.corners[0].astype(int)), 4, (0, 0, 255), 2) # left-top
            cv2.circle(frame, tuple(tag.corners[1].astype(int)), 4, (0, 0, 255), 2) # right-top
            cv2.circle(frame, tuple(tag.corners[2].astype(int)), 4, (0, 0, 255), 2) # right-bottom
            cv2.circle(frame, tuple(tag.corners[3].astype(int)), 4, (0, 0, 255), 2) # left-bottom

            apriltag_width = abs(tag.corners[0][0] - tag.corners[1][0]) / 2
            target_x = apriltag_width / 2

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cap.set(3,320)
    cap.set(4,320)
    cap.set(5,120)
    ad = ApriltagDetect()
    while True:
        ret, frame = cap.read()
        frame = cv2.rotate(frame, cv2.ROTATE_180)
        ad.update_frame(frame)
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
