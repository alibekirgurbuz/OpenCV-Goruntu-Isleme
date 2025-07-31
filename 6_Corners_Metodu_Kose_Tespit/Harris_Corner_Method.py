import cv2
import numpy as np

# Görüntüyü yükle
img = cv2.imread('../Assets/vazo.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# float32 tipine dönüştür
gray = np.float32(gray)

# Harris köşe tespiti
"""
blockSize: Köşe tespiti için kullanılan komşuluk alanının boyutu.
ksize: Sobel türevleri için çekirdek boyutu.
k: Harris algılayıcısı için serbest parametre (genellikle 0.04–0.06 arası).
"""
dst = cv2.cornerHarris(gray, blockSize=7, ksize=3, k=0.05)

# Sonuçları genişlet (güçlü köşeler için eşik uygula)
img[dst > 0.01 * dst.max()] = [0, 0, 255]
img = cv2.resize(img,(500,500))
cv2.imshow('Köşe Tespiti', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
