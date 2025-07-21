import cv2
import numpy as np

img = cv2.imread("../Djital_Goruntu_Nedir/pp.jpg")
b, g, r = img[100, 200]  # 100. satır, 200. sütun
print("B:", b, "G:", g, "R:", r)
img[100, 200] = [0, 72, 0]
cv2.imshow("pp",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

