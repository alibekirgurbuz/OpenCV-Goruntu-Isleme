import cv2

cap =cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier("../12_Cascade_Islemleri!!/haarcascade_frontalface_default.xml")
mouth_cascade= cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gri,1.1,8)
    if len(faces )== 0:
        cv2.putText(frame,"yüz tespit edilmedi",(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255))

    else:
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            roi_gri = gri[y:y+h,x:x+w]
            mouth = mouth_cascade.detectMultiScale(roi_gri, 1.4, 20)

            if len(faces) == 0:
                cv2.putText(frame, "maske var", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255))
            else:
                for x1,y1,w1,h1 in mouth:
                    cv2.rectangle(frame, (x1+x, y1+y), (x1 + w1 + x, y1 + h1 + y), (0, 255, 255), 3)
                    cv2.putText(frame, "maske yok", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))


    cv2.imshow("a", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()