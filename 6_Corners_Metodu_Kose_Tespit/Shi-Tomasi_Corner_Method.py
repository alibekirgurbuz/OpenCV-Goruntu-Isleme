"""
Harris’e alternatif olarak geliştirilmiştir,
OpenCV’de “Good Features to Track” olarak da geçer
ve daha güvenilir sonuçlar verir.
"""

import cv2
import numpy as np

img = cv2.imread('../1_Djital_Goruntu_Nedir/pp.jpg')
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""
maxCorners: Algılanacak maksimum köşe sayısı.
qualityLevel: Algılanacak köşelerin kalite eşiği (0–1 arası).
minDistance: Tespit edilen köşeler arasındaki minimum mesafe.
"""

corners = cv2.goodFeaturesToTrack(gri, maxCorners=1000, qualityLevel=0.01, minDistance=100)
corners = corners.astype(int)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (0,255,0), -1)
img=cv2.resize(img,(500,500))
cv2.imshow('Shi-Tomasi Köşe Tespiti', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
