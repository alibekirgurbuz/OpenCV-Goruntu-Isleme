import cv2
import numpy as np

img = cv2.imread("../Assets/sekil.png")
img = cv2.resize(img, (500, 500))

font = cv2.FONT_HERSHEY_COMPLEX
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gri, 200, 255, cv2.THRESH_BINARY)
kontur, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in kontur:
    e = 0.01 * cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, e, True)
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)

    x, y = approx.ravel()[0], approx.ravel()[1]

    label = "daire"
    if len(approx) == 3:
        label = "3"
    elif len(approx) == 4:
        label = "4"
    elif len(approx) == 5:
        label = "5"
    elif len(approx) == 6:
        label = "6"
    elif len(approx) == 7:
        label = "7"
    elif len(approx) == 8:
        label = "8"

    cv2.putText(img, label, (x, y + 20), font, 1, (0, 0, 0), 1)

cv2.imshow("Sekil Algilama", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
