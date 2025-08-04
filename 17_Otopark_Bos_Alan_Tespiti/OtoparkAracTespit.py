import cv2
import numpy as np
import pickle

cap = cv2.VideoCapture("../Assets/video.mp4")

def check(frame1):
    spacecounter = 0
    for pos in liste:
        x1, y1 = pos
        crop = frame1[y1:y1 + 15, x1:x1 + 26]
        count = cv2.countNonZero(crop)
        #print(f"Boş alan sayısı: {count}")
        if count<150:
            color = (0,255,0)
            spacecounter += 1
        else:
            color =[0,0,255]
        cv2.rectangle(frame, pos,(pos[0]+25,pos[1]+15), color, 2)
    cv2.putText(frame, f"Bos: {spacecounter}/{len(liste)}", (15,24), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)

with open("noktalar", "rb") as f:
    liste = pickle.load(f)

while True:
    _,frame = cap.read()
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gri, (3, 3),1,)
    thres = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    median = cv2.medianBlur(thres, 5)
    dilates = cv2.dilate(median, np.ones((3, 3), np.uint8), iterations=1)

    check(dilates)

    cv2.imshow("asd",frame)

    if cv2.waitKey(200) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()