import cv2

img = cv2.imread("subtle.jpg",0) 
			# pass 1 for reading the image as it is
			# pass 0 for geyscale
			# pass -1 for as it is + alpha colour capabilities

print(img)			
print(img.shape)	#print resolutions px by px
print(img.ndim)  #no of colour dimensions of the array

img2 = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
print(img2.shape)
cv2.imshow("Architecture",img2)
cv2.waitKey(15000)
cv2.destroyAllWindows()
