import cv2

model = cv2.CascadeClassifier("../haarcascade_frontalface_default.xml")

img = cv2.imread("multiface.jpeg")
greyimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = model.detectMultiScale(greyimg,scaleFactor = 1.10,minNeighbors = 2)

print(faces)

for x,y,w,h in faces:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,240,0),2)



cv2.imshow("Many Faces",img)
cv2.waitKey(3000)
cv2.destroyAllWindows()