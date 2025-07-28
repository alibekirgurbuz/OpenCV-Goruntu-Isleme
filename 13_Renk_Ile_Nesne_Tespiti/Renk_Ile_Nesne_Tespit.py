import cv2 # OpenCV kütüphanesi, görüntü işleme için kullanılır.
import numpy as np # Dizi işlemleri için.
from collections import deque # Nesnenin izini takip etmek için sabit uzunlukta bir liste (kuyruk yapısı).

buffer_size = 16  # Ekranda son 16 konumu hatırlamak için kullanılır.
pts = deque(maxlen=buffer_size) # Bu noktalar deque içine eklenerek iz oluşturur.


# Belirli bir mavi renk aralığı (HSV formatında).
# Bu aralık, tespit edilmek istenen nesnenin rengine göre ayarlanır.
blue_lower = np.array([84,98,0])
blue_upper =np.array([179,255,255])

cap = cv2.VideoCapture(0)

cap.set(3,760) # Genişlik
cap.set(4,380) # Yükseklik

while True:
    # Kameradan görüntü alınır.
    # success: Görüntü alınabildiyse True döner.
    success, imgorginal =cap.read()

    if success:
        # Görüntü bulanıklaştırılır (gürültü azaltma).
        # BGR'den HSV renk uzayına dönüştürülür.
        blurred = cv2.GaussianBlur(imgorginal,(11,11),0)
        hsv =cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
        cv2.imshow("hsvpencere",hsv)

        # Maskeleme işlemi
        # Belirli renk aralığındaki pikseller mask içinde beyaz olur.
        # erode: Gürültüyü temizler.
        # dilate: Nesnenin alanını genişletir.
        mask = cv2.inRange(hsv,blue_lower,blue_upper)
        mask = cv2.erode(mask, np.ones((3, 3), np.uint8), iterations=2)
        mask = cv2.dilate(mask,np.ones((3, 3), np.uint8),iterations=2)

        cv2.imshow("maskeli Pencere",mask)

        # Kontur bulma ve en büyük kontur ile çalışma
        # mask üzerinde konturlar (nesne sınırları) bulunur.
        # RETR_EXTERNAL: Sadece dış konturları alır.

        (contours,_) = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        center = None

        # Eğer kontur varsa, en büyük olanı (max area) seçilir.
        if len(contours) > 0:
            c = max(contours,key=cv2.contourArea)

            # Nesne bilgileri ve çizim
            # Tespit edilen nesneye minimum dikdörtgen oturtulur.
            # Bu dikdörtgenin merkezi, boyutları ve dönüş açısı alınır.
            rect = cv2.minAreaRect(c)
            ((x,y),(width,height),rotation) = rect
            s= "x:{}, y:{}, width:{}, height:{}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            print(s)

            # box: Dikdörtgenin 4 köşesi.
            # drawContours: Bu kutu ekranda çizilir.
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            # Moment hesabı ile konturun merkezi (center) bulunur.
            M = cv2.moments(c)

            if M["m00"] != 0:  # sıfıra bölme hatası önleniyor
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                cv2.drawContours(imgorginal, [box], 0, (0, 255, 255), 2)
                cv2.circle(imgorginal, center, 5, (255, 0, 0))
                pts.append(center)
            else:
                center = None
        # İz bırakma (Trajectory)
        # pts dizisine merkez noktalar eklenir.
        # Bu noktalar arası çizgi çizilerek nesnenin hareketi izlenir.
        for i in range(1,len(pts)):
            if pts[i-1] is None or pts[i] is None:continue
            cv2.line(imgorginal,pts[i-1],pts[i],(0,255,255),3)
        cv2.imshow("orijinal", imgorginal)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

"""
 OpenCV kullanarak bir kameradan canlı görüntü alır ve belirli bir renk
aralığında nesne tespiti yapar. Kod aynı zamanda nesnenin hareketini takip eder ve iz bırakır
"""