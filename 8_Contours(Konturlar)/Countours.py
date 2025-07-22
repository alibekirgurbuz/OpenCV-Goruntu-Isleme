"""
Kontur, bir şeklin dış hatlarını yani sınır çizgisini belirtir.
Genellikle kenar tespitinden sonra uygulanır.
Contours işlemleri şu amaçlarla kullanılır:
- Nesne tespiti ve segmentasyonu
- El hareketi takibi
- Hareketli nesne tespiti
- Optik karakter tanıma (OCR) ön işlemi
"""
import cv2

# Görüntüyü oku
img = cv2.imread('vazo.jpg')

# Griye çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary görüntü elde et:
"""
OpenCV'deki eşikleme (thresholding) işlemini gerçekleştirir.
Görüntü işleme sürecinde, gri seviyeli bir görüntüyü siyah-beyaz
(binary) hale getirmek için kullanılır.
-> cv2.threshold(): Bu fonksiyon, her bir pikselin değerini kontrol eder
ve belirli bir eşik değerine göre onu 0 ya da belirlenen
maksimum değere (genelde 255) dönüştürür.

thresh: Eşik değeri (örnekte 127),
maxval:	Eşik geçildiğinde verilecek maksimum değer (örnekte 255)
type:	Eşikleme türü (örnekte cv2.THRESH_BINARY)
ret:	Eşikleme sonucu dönen eşik değeri (genelde önemli değil)
thresh:	Eşiklenmiş (binary) görüntü çıktısı  => ret, thresh buradaki tresh
"""
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Konturları bul
"""
findContours(), siyah-beyaz (binary) bir görüntüde beyaz alanların sınırlarını bulur.
Her bir kontur, bir şeklin ya da nesnenin kenarını temsil eden bir koordinat dizisidir (numpy array).

PARAMETRELERİ: 
'cv2.findContours(image, mode, method)'

image:
Eşiklenmiş (binary) görüntü (thresh)

mode: (Kontur alma yöntemi)
cv2.RETR_EXTERNAL :>	Sadece en dıştaki konturları bulur.
cv2.RETR_TREE :>	Tüm konturları ve hiyerarşiyi bulur (iç içe nesneler için idealdir).
cv2.RETR_LIST :>	Tüm konturları alır ama hiyerarşi yoktur.

method: (Kontur basitleştirme)
cv2.CHAIN_APPROX_NONE :> Tüm piksel noktalarını alır (yoğun veri).
cv2.CHAIN_APPROX_SIMPLE :>	Gereksiz noktaları kaldırır (daha az veri, daha hızlı).

contours: Her bir kontur, koordinat noktalarının bulunduğu bir numpy array listesidir.
hierarchy: Konturların birbirine göre hiyerarşisini verir.
"""
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Konturları çiz
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Görüntüyü göster
img=cv2.resize(img,(500,500))
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

