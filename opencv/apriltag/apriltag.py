import cv2
import pupil_apriltags as apriltag
import time

video = 0
cap = cv2.VideoCapture(video)
cap.set(3,320)
cap.set(4,320)
cap.set(5,120)

# 创建一个apriltag检测器，然后检测AprilTags
options = apriltag.Detector(families='tag36h11')  # windows

while True:
    success,image = cap.read()
    t1=time.time()
    if success:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        results = options.detect(gray)
        if results:
            for r in results:
                # 获取4个角点的坐标
                b = (tuple(r.corners[0].astype(int))[0], tuple(r.corners[0].astype(int))[1])
                c = (tuple(r.corners[1].astype(int))[0], tuple(r.corners[1].astype(int))[1])
                d = (tuple(r.corners[2].astype(int))[0], tuple(r.corners[2].astype(int))[1])
                a = (tuple(r.corners[3].astype(int))[0], tuple(r.corners[3].astype(int))[1])

                # 绘制检测到的AprilTag的框
                cv2.line(image, a, b, (255, 0, 255), 2, lineType=cv2.LINE_AA)
                cv2.line(image, b, c, (255, 0, 255), 2, lineType=cv2.LINE_AA)
                cv2.line(image, c, d, (255, 0, 255), 2, lineType=cv2.LINE_AA)
                cv2.line(image, d, a, (255, 0, 255), 2, lineType=cv2.LINE_AA)

                # 绘制 AprilTag 的中心坐标
                (cX, cY) = (int(r.center[0]), int(r.center[1]))
                cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)

                # 在图像上绘制标文本
                tagFamily = r.tag_family.decode("utf-8")
                cv2.putText(image, tagFamily, (a[0], a[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 255, 0), 2)
    t2=time.time()
    if (t2 - t1):
        print(1/(t2 - t1))
    cv2.imshow("Image", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
