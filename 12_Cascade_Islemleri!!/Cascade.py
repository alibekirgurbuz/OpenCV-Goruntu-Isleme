import cv2

orj = cv2.imread("../Assets/sean2.jpg")
orj = cv2.resize(orj,(400,300))

img = cv2.imread("../Assets/sean2.jpg")
img = cv2.resize(img,(400,300))
yuz = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces =yuz.detectMultiScale(gri,1.3,4)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("orj",orj)
cv2.imshow("Cascaded",img)
cv2.waitKey(0)

cv2.destroyAllWindows()
