import cv2

img = cv2.imread("../1_Djital_Goruntu_Nedir/pp.jpg")
y, x = 100, 200
b, g, r = img[y, x]
print(f"B: {b} ({format(b, '08b')})") ## 8-bit binary olarak formatla
print(f"G: {g} ({format(g, '08b')})")
print(f"R: {r} ({format(r, '08b')})")
