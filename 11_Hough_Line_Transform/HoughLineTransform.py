import cv2
import numpy as np

def update(val):
    # Trackbar değerlerini oku
    threshold = cv2.getTrackbarPos("Threshold", "Hough Lines")
    min_line_length = cv2.getTrackbarPos("Min Line Length", "Hough Lines")
    max_line_gap = cv2.getTrackbarPos("Max Line Gap", "Hough Lines")
    canny_low = cv2.getTrackbarPos("Canny Lower", "Hough Lines")
    canny_high = cv2.getTrackbarPos("Canny Upper", "Hough Lines")

    # Görüntüyü kopyala
    temp_img = img.copy()

    # Kenar tespiti
    edges = cv2.Canny(gray, canny_low, canny_high)

    # Çizgi tespiti
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold,
                            minLineLength=min_line_length, maxLineGap=max_line_gap)

    # Çizgileri çiz
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(temp_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Görüntüyü göster
    cv2.imshow("Hough Lines", temp_img)

# Görüntüyü yükle ve griye çevir
img = cv2.imread('../Assets/hough.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Pencere oluştur
cv2.namedWindow("Hough Lines")

# Trackbarları oluştur
cv2.createTrackbar("Threshold", "Hough Lines", 30, 150, update)
cv2.createTrackbar("Min Line Length", "Hough Lines", 50, 300, update)
cv2.createTrackbar("Max Line Gap", "Hough Lines", 10, 100, update)
cv2.createTrackbar("Canny Lower", "Hough Lines", 50, 255, update)
cv2.createTrackbar("Canny Upper", "Hough Lines", 150, 255, update)

# İlk güncelleme
update(0)

# Tuşa basılana kadar bekle
cv2.waitKey(0)
cv2.destroyAllWindows()
