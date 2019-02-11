import cv2
import time

model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

check,frame = video.read()   #reading from camera

print(check)
print(frame)


grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #converting captured image to greyScale

cv2.imshow("raw grey ",grey)
cv2.waitKey(2000)
cv2.destroyAllWindows()
#cv2.imwrite("facegrey.jpg",grey)   #to save image if necessary

#img = cv2.imread("facegrey.jpg",0)  # reading saved image
face = model.detectMultiScale(grey,scaleFactor=1.05,minNeighbors=5)  #checking for face


print(face)

for x,y,w,h in face:			#draing rectangle around faces
	frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,240,0),3)

cv2.imshow("face on frame",frame)  #displaying the frames with rectangles around them
cv2.waitKey(5000)
cv2.destroyAllWindows()	

video.release()