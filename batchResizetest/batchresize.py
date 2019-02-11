import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
	im=cv2.imread(image,0)
	re=cv2.resize(im,(100,100))
	cv2.imshow("hey",re)
	cv2.waitKey(1000)
	cv2.destroyAllWindows()
	cv2.imwrite("resized_"+image,re)
