import cv2
import pickle
# Otopark park alanı tespiti için nokta ekleme ve silme uygulaması

# Bu try except bloğu önceden kaydedilmiş nokta listesini yükler.
# Eğer dosya yoksa, boş bir liste oluşturur.
try:
    with open ("noktalar", "rb") as f:
        liste = pickle.load(f)
except:
    liste=[]

def mouse(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        liste.append((x, y)) # Sol tıkla (x, y) koordinatlarını listeye ekler

    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(liste):
            x1, y1 = pos
            if x1<x<x1 + 26 and y1<y<y1 + 15:
                liste.pop(i) # Tıklanan konumda 26x15 piksel dikdörtgen içinde işaretleyici varsa siler

    with open("noktalar", "wb") as f:
        pickle.dump(liste, f)


while True:
    img = cv2.imread("../Assets/first_frame.png")

    for I in liste:
        cv2.rectangle(img, I, ( I[0]+26, I[1]+15), (255,0, 0), 2) # Liste içindeki her nokta için 26x15 piksel boyutunda dikdörtgen çizer


    cv2.imshow("img", img)
    cv2.setMouseCallback("img", mouse)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
