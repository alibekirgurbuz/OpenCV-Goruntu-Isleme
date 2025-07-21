"""
Canny Kenar Tespit Algoritması, dijital görüntülerdeki
kenarları tespit etmek için geliştirilmiş bir görüntü işleme algoritmasıdır.
1986 yılında John F. Canny tarafından geliştirilmiştir
ve günümüzde en popüler kenar tespit yöntemlerinden biridir.
"""

import cv2

# 1. Görüntüyü oku
img = cv2.imread('../1_Djital_Goruntu_Nedir/pp.jpg')

# 2. Griye dönüştür
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Gaussian blur uygula
blur = cv2.GaussianBlur(gray, (5, 5), 1)

# 4. Canny algoritmasını uygula
# (düşük eşik, yüksek eşik)
edges = cv2.Canny(blur, 50, 150)

# 5. Sonuçları göster
img=cv2.resize(img,(500,500))
edges=cv2.resize(edges,(500,500))

cv2.imshow("Orijinal", img)
cv2.imshow("Canny Kenarları", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
