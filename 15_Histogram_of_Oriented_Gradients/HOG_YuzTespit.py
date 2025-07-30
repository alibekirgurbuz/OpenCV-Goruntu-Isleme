import cv2
import face_recognition


image = cv2.imread("sean.jpg")

facelocs = face_recognition.face_locations(image, model="hog")

for index,facelocs in enumerate(facelocs):
    toplefty,bottomrightx,bottomrihty,topleftx = facelocs
    detectedface =image[toplefty:bottomrihty,topleftx:bottomrightx]
    cv2.imshow("detface",detectedface)
cv2.waitKey()
cv2.destroyAllWindows()