import cv2

model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#the xml file is a trained model used to comapre pictures for face similarity 
#thus finding a face in a picture

img = cv2.imread("portraitLady.jpg") #no 2nd parameter as we are keeping the original color
img = cv2.resize(img,(700,500))
greyimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
greyimg = cv2.resize(greyimg,(700,500))

face = model.detectMultiScale(greyimg,scaleFactor=1.10,minNeighbors=5)
print(type(face))
print(face)

for x,y,w,h in face:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,240,0),1)
					                        #(B,G,R),thickness

cv2.imshow("grey",img)
cv2.waitKey(3000)
cv2.destroyAllWindows()