import cv2
import time

video = cv2.VideoCapture(0)  

a=1   #to calculate frames

while True:
	check , frame = video.read()		#check is capture is true, frame is the input image
	a=a+1
	print(check)
	print(frame)
	
	grey =frame
	#grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   #to convert to greyScale
	#time.sleep(3)   #output time delay
	
	cv2.imshow("Video capture", grey)   #display the captured image(s)

	key = cv2.waitKey(1)  #key - to set an exit hotkey, 1 (1 millisec) refresh rate

	if key==ord("q"):  #exit when q is pressed
		break

print("Total frames = " + str(a))  
video.release()   #idk
cv2.destroyAllWindows()	