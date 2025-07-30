import cv2
import face_recognition

cap = cv2.VideoCapture(0)

while True:
    _,frame =cap.read()
    facelocs = face_recognition.face_locations(frame, model="hog")

    for index, facelocs in enumerate(facelocs):
        toplefty, bottomrightx, bottomrihty, topleftx = facelocs
        detectedface = frame[toplefty:bottomrihty, topleftx:bottomrightx]
        cv2.imshow("detface", detectedface)
        cv2.imshow("orj", frame)
    if cv2.waitKey(6) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()