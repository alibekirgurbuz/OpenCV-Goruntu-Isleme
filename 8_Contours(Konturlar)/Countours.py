import cv2

# Görüntüyü oku
orj = cv2.imread('../Assets/vazo.jpg')
img = cv2.imread('../Assets/vazo.jpg')

# Griye çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary görüntü elde et:
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Konturları bul
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Konturları çiz
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Görüntüyü göster
img=cv2.resize(img,(500,500))
orj=cv2.resize(orj,(500,500))

cv2.imshow("Contours", img)
cv2.imshow("Orijinal",orj)
cv2.waitKey(0)
cv2.destroyAllWindows()

