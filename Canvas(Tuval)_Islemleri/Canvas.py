import cv2
import numpy as  np

"""
numpy.zeros() fonksiyonu, belirli boyutlarda tüm değerleri sıfır olan (yani siyah) bir NumPy dizisi oluşturur.
OpenCV’de bu diziyi görüntü gibi kullanarak üzerine çizim yapabilirsin.

canvas = np.zeros(shape, dtype) 

- shape: Tuvalin boyutları (yükseklik, genişlik) veya (yükseklik, genişlik, kanal).
- dtype: Veri tipi (görüntüler için genelde np.uint8 kullanılır).
"""

canvas = np.zeros((300, 600, 3), dtype=np.uint8) +255 # 300 piksel yüksek, 600 geniş, 3 kanal (BGR) +255 ifadesi tuvalin rengini beyaz yapar.

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
