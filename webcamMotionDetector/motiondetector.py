import cv2, time


#to store the first frame in a NummPy static variable
first_frame = None

video = cv2.VideoCapture(0)

a=0

while True:

	a=a+1;
	check,frame = video.read()

	grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	greygb = cv2.GaussianBlur(grey,(21,21),0)
									#width n height of the gaussian kernel, deviation parameter


	if first_frame is None:
		first_frame = grey   # to store the first frame which will be used as refrence for difference 
		continue

	delta = cv2.absdiff(first_frame,greygb)	  #absolute difference

	cv2.imshow("Video - GreyScale",grey)
	cv2.imshow("Grey Blurred",greygb)
	cv2.imshow("delta", delta)

	key = cv2.waitKey(1)
	print(grey)

	if key == ord ('q'):
		break

print("Total Frames Captured : " + str(a))
video.release()
cv2.destroyAllWindows()		