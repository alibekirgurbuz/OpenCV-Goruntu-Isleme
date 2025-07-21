import cv2

# cv2.VideoCapture(0) (kamera için)
cap = cv2.VideoCapture(0)

"""
Videolar bir bütün olarak opencv ile yakalanmayacağı için döngü içerisinde frame' ler
yakalanmalıdır. 
"""

# ret: Okuma başarılıysa True, başarısızsa False döner.
# #frame: Okunan görüntü karesi (NumPy array).

while True:
    ret, frame = cap.read()   # Frame oku
    if not ret:
        break                # Video bitti veya hata oluştu
    frame=cv2.flip(frame,1)
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()     # Video kaynağını serbest bırak
cv2.destroyAllWindows()