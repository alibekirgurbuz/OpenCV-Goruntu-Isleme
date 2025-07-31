import cv2

# Görüntüyü yükle
image = cv2.imread('../Assets/vazo.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Konturları bul
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Kontur üzerinde dön
for cnt in contours:
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])

        # Merkeze kırmızı daire çiz
        cv2.circle(image, (cx, cy), 5, (0, 0, 255), -1)
        cv2.putText(image, f"({cx},{cy})", (cx+10, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)

# Görüntüyü göster
cv2.imshow("Merkezler", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

