import cv2
import time

video = cv2.VideoCapture(0)

check,frame = video.read()

print(check)
print(frame)

time.sleep(3)

grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

cv2.imshow("VID",grey)
cv2.waitKey(0)
cv2.destroyAllWindows()

video.release()

