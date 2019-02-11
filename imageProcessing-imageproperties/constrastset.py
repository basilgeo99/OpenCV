import cv2
import numpy as np

# Open a typical 24 bit color image. For this kind of image there are
# 8 bits (0 to 255) per color channel
imgx = cv2.imread('mandrill.png')  # mandrill reference image from USC SIPI

img = cv2.cvtColor(imgx,cv2.COLOR_BGR2GRAY)

cv2.imwrite("imgx in grey.png",img)

method = 'numpy_way'   # or 'opencv_way'

if method == 'numpy_way':
    # Convert to signed 16 bit. this will allow values less than zero and
    # greater than 255
    img = np.int16(img)  

    contrast   = 64
    brightness = 0

    img = img*(contrast/150 + 1) - contrast + brightness

    # we now have an image that has been adjusted for brightness and
    # contrast, but we need to clip values not in the range 0 to 255
    img = np.clip(img, 0, 255)  # force all values to be between 0 and 255

    # finally, convert image back to unsigned 8 bit integer
    img = np.uint8(img)
elif method == 'opencv_way':
    b = 64. # brightness
    c = 0.  # contrast

    #call addWeighted function, which performs:
    #    dst = src1*alpha + src2*beta + gamma
    # we use beta = 0 to effectively only operate on src1
    img = cv2.addWeighted(img, 1.0 + c/127., img, 0, b-c)

cv2.imwrite('mandrill_contrast64.png', img)