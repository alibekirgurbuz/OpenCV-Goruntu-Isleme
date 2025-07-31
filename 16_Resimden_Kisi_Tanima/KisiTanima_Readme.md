`face_recognition`, Python diliyle yazılmış,
kolay kullanımlı bir yüz tanıma (face recognition)
kütüphanesidir. Arkasında dlib tabanlı bir yüz tanıma
modeli çalışır ve _günümüzde bilinen en doğru açık kaynak
yüz tanıma sistemlerinden biridir._

## Temel Özellikler

1. Yüz tespiti (face detection)
2. Yüzlerin yerini belirleme (face location)
3. Yüz karşılaştırma (face comparison)
4. Yüz encoding (face encoding)
5. Yüz tanıma (face recognition)
6. Yüz üzerinde belirli noktaların bulunması (facial landmarks)

`dlib` kütüphanesinin 68 noktalı yüz landmark modeli kullanılır.
HOG (Histogram of Oriented Gradients) veya CNN tabanlı yüz algılama
seçenekleri mevcuttur.

**Not:** dlib bağımlılığı olduğu için, Windows kullanıcıları
precompiled wheel dosyalarını tercih etmeli veya _CMake_ ile
derlemelidir. `pip install cmake`

Alternatifler: 
mediapipe, deepface