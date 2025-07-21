import cv2
img = cv2.imread("../1_Djital_Goruntu_Nedir/pp.jpg")

"""
cv2.resize(), verilen bir görüntüyü yeni bir boyuta
genişlik ve yükseklik) ölçeklendirmek (yeniden boyutlandırmak)
için kullanılır.
PARAMETRELERİ:
-src (zorunlu): Yeniden boyutlandırılacak kaynak görüntü (NumPy array).
-dsize (zorunlu): Hedef boyut (genişlik, yükseklik) şeklinde tuple olarak girilir.
"""

img = cv2.resize(img,(400,300))

"""
Oluşturulan pencereye isim vermek için kullanılır.
flags:
- cv2.WINDOW_NORMAL: Pencereyi yeniden boyutlandırabilirsin.
- cv2.WINDOW_AUTOSIZE (varsayılan): Pencere otomatik boyutlanır
ve yeniden boyutlandırılamaz.
"""
cv2.namedWindow("Profil_Fotografi", cv2.WINDOW_NORMAL)
cv2.imshow("Profil_Fotografi",img)

while True:
    # Pencerenin "Profil_Fotografi" adıyla açık olup olmadığını kontrol et
    if cv2.getWindowProperty("Profil_Fotografi", cv2.WND_PROP_VISIBLE) < 1:
        break
    # Klavyeden 'q' tuşuna basılırsa döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

