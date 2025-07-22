"""
Convex Hull (Dışbükey Zarf), bir nesnenin veya noktalar
kümesinin etrafını saran en küçük dışbükey çokgendir.
 Bu çokgen, içerideki tüm noktaları veya nesnenin sınırını tamamen kapsar
ve içe çökme (concavity) noktalarını atlar.
Görüntü işleme ve nesne tespitinde, özellikle el, yüz
veya genel şekil analizinde sıklıkla kullanılır.
"""

import cv2
import numpy as np

img = cv2.imread("../8_Contours(Konturlar)/vazo.jpg")
img = cv2.resize(img,(500,500))
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gri,75,200,cv2.THRESH_BINARY)

contur, h = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
h =list()

for i in range(len(contur)):
    h.append(cv2.convexHull(contur[i],False))
z = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)

for i in range(len(contur)):
    cv2.drawContours(z,contur,i,(255,0,0),3,8)
    cv2.drawContours(z,h,i,(0,255,0),1,8)


cv2.imshow("vazo",z)
cv2.waitKey(0)
cv2.destroyAllWindows()