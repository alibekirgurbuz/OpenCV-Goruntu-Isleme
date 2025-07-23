import cv2

# 1. Haar cascade sınıflandırıcı dosyasını yükle
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. Kameradan görüntü almak için VideoCapture başlat
cap = cv2.VideoCapture(0)  # 0 varsayılan kamerayı açar

while True:
    # 3. Kameradan bir kare al
    ret, frame = cap.read()
    if not ret:
        break

    # 4. Görüntüyü gri tonlamalıya çevir (tespit işlemi için)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. Yüz tespiti yap
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # 6. Tespit edilen yüzleri dikdörtgenle çiz
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # 7. Sonuç görüntüsünü göster
    cv2.imshow('Live Face Detection', frame)

    # 8. Çıkmak için 'q' tuşuna basılmasını bekle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 9. Kaynakları serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
