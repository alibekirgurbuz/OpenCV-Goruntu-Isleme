import cv2
import numpy as np

img = cv2.imread("../Assets/pp.jpg")
b, g, r = img[100, 200]  # 100. satır, 200. sütun

print("B:", b, "G:", g, "R:", r)
img[100, 200] = [0, 72, 0] # 100. satır, 200. sütundaki pikselin rengini "0, 72, 0" ile değiştiriyor.
cv2.imshow("pp",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

