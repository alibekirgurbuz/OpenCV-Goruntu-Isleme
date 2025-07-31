import cv2
from skimage.feature import hog
from skimage import exposure

image = cv2.imread("../Assets/sean.jpg")
image = cv2.resize(image,(400,300))

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_,hogimage = hog(gray,visualize=True)
hogimage = cv2.resize(hogimage,(400,300))

rescaled = exposure.rescale_intensity(hogimage, in_range=(0,10))
rescaled = cv2.resize(rescaled,(400,300))


cv2.imshow("hog",hogimage)
cv2.imshow("orj",image)
cv2.imshow("resc",rescaled)



cv2.waitKey(0)
cv2.destroyAllWindows()