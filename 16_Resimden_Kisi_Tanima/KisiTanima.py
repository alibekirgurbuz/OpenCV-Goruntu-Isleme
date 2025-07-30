import face_recognition
import cv2

# Bilinen yüz görüntülerini yükle (veritabanı)
image_sean = face_recognition.load_image_file("../15_Histogram_of_Oriented_Gradients/sean.jpg")
image_clint = face_recognition.load_image_file("../15_Histogram_of_Oriented_Gradients/clint.jpg")

# Encode işlemi
encoding_sean = face_recognition.face_encodings(image_sean)[0]
encoding_clint = face_recognition.face_encodings(image_clint)[0]

# Bilinen yüz vektörleri ve adlar listesi
known_face_encodings = [encoding_sean, encoding_clint]
known_face_names = ["sean", "clint"]

# Tanınacak test görüntüsü
test_image = face_recognition.load_image_file("../15_Histogram_of_Oriented_Gradients/clint2.jpg")
test_image_rgb = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)

# Yüz tespiti ve encoding
face_locations = face_recognition.face_locations(test_image_rgb)
face_encodings = face_recognition.face_encodings(test_image_rgb, face_locations)

# OpenCV ile görüntüyü BGR formatına çevir
image_bgr = cv2.cvtColor(test_image_rgb, cv2.COLOR_RGB2BGR)

# Her yüz için kontrol yap ve etiketle
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Tanınmadı"

    # Eşleşme varsa ilk eşleşen kişinin adını al
    if True in matches:
        match_index = matches.index(True)
        name = known_face_names[match_index]

    # Yüzü dikdörtgen içine al ve ismini yaz
    cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(image_bgr, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

# Sonuç görüntüsünü göster
cv2.imshow("Yüz Tanıma Sonucu", image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
