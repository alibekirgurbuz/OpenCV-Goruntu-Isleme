"""
Görüntüyü Okuma ve Görüntüleme
"""

# openCV kütüphanesini kullanabilmek için cv2 yi import ediyoruz.
import cv2

"""
cv2.imread(filename, flags), belirtilen dosya yolundaki görüntüyü okur ve bir NumPy dizisi (matris) olarak döndürür.
filename (zorunlu): Okunacak görüntü dosyasının yolu veya adı.
flags (isteğe bağlı): Görüntünün nasıl okunacağını belirleyen parametredir. En sık kullanılan Flags(Bayraklar) : 
(cv2.IMREAD_COLOR) veya 1, 'Görüntüyü BGR renkli olarak okur. Alfa (şeffaflık) kanalı varsa yok sayılır.'
(cv2.IMREAD_GRAYSCALE) veya 0, 'Görüntüyü siyah-beyaz (gri tonlu) olarak okur.'
(cv2.IMREAD_UNCHANGED) veya -1  Dosyadaki tüm kanalları olduğu gibi okur (ör: RGBA).
"""
# Görüntüyü oku (grayscale olarak)
img = cv2.imread('pp.jpg',0)

"""
.shape özelliği, (.shape bir fonksiyon değildir, bir özelliktir. Parantez kullanılmaz: img.shape)
bir NumPy dizisinin (ve dolayısıyla OpenCV ileokunan bir görüntünün)
boyutlarını (satır, sütun ve kanal sayısı) döndürür.
- Gri tonlu görüntülerde: (yükseklik, genişlik)
- Renkli görüntülerde: (yükseklik, genişlik, kanal_sayısı)
"""

print("Görüntü boyutu:", img.shape)  # (satır, sütun)
print("Birinci pikselin değeri:", img[0, 0])

# imshow() fonksiyonu ile görüntü ekranda gösterilir
cv2.imshow("Gri Tonlu Görüntü", img)

"""
cv2.waitKey(), OpenCV’de bir pencere (window) açıkken,
klavyeden bir tuşa basılmasını belirli bir süre bekleyen bir fonksiyondur.
Genellikle cv2.imshow() fonksiyonu ile birlikte kullanılır.
"""

cv2.waitKey(0)

"""
cv2.destroyAllWindows(), OpenCV ile açılmış olan
tüm pencereyi (window) kapatmaya yarayan bir fonksiyondur.
"""
cv2.destroyAllWindows()