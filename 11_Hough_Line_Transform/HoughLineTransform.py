"""
Hough Line Transform, OpenCV’de çizgi tespiti için en çok kullanılan yöntemlerden biridir.
özellikle yol şeritleri, kenarlar veya yapısal çizgiler gibi doğrusal şekilleri bulmak için kullanılır.

-> cv2.HoughLines() → Klasik Hough Transform
-> cv2.HoughLinesP() → Probabilistic (Olasılıksal) Hough Transform (daha pratik ve hızlıdır)
"""

import cv2
import numpy as np

img = cv2.imread('hough.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3) # Çizgi tespiti için önce kenar tespiti yapılmalı.

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, minLineLength=50, maxLineGap=10)
# minLineLength: Tespit edilecek minimum çizgi uzunluğu
# maxLineGap: Aynı doğru üzerinde kabul edilebilecek maksimum boşluk
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Hough Lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
