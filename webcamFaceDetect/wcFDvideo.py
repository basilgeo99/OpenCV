import cv2
import time

model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)


a=1

while True:

	check,frame=video.read()
	a=a+1
	print(check)
	print(frame)

	grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	face = model.detectMultiScale(grey,scaleFactor=1.05,minNeighbors=5)

	print(face)

	for x,y,w,h in face:
		frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,240,0),2)

	cv2.imshow("Face Detection on video",frame)
	
	key=cv2.waitKey(1)

	

	if key==ord("q") :
		break

print("Total frames = "+str(a))

video.release()
cv2.destroyAllWindows()