import cv2

# Yüz ve göz Haar Cascade dosyalarını yükle
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        # Yüzün etrafını mavi bir dikdörtgenle çiz
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Yüz bölgesinin içinde göz araması yap
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        for (ex, ey, ew, eh) in eyes:
            # Gözlerin etrafını yeşil bir dikdörtgenle çiz
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('Face and Eye Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
