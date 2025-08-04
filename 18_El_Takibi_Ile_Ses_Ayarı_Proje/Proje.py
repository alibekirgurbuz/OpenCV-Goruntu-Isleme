import cv2
import mediapipe as mp
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# mediapipe için python un sürümü  3.9 ve üstü olmalıdır.

# Ses kontrol ayarları bu kısımda yapılır
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol_min, vol_max = volume.GetVolumeRange()[:2]  # dB cinsinden

# MediaPipe elleri başlat
# Elin her parmağındaki 21 anahtar nokta tespit edilir.
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# Kamera başlat
cap = cv2.VideoCapture(0)

def calculate_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(handLms.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))

    if lmList:
        # Baş parmak ucu (id=4), işaret parmak ucu (id=8)
        x1, y1 = lmList[4]
        x2, y2 = lmList[8]
        length = calculate_distance((x1, y1), (x2, y2))

        # Minimum ve maksimum mesafe aralığı
        min_dist = 20
        max_dist = 200
        length = np.clip(length, min_dist, max_dist)

        # Ses düzeyi ayarlamaları
        vol_percent = np.interp(length, [min_dist, max_dist], [0, 100])
        vol_bar = np.interp(length, [min_dist, max_dist], [400, 150])
        vol_set = np.interp(length, [min_dist, max_dist], [vol_min, vol_max])
        volume.SetMasterVolumeLevel(vol_set, None)

        # Görsel geri bildirimlerin ayarlanması bu ksımda yapılır
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 3)
        cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, f'{int(vol_percent)} %', (40, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

    cv2.imshow("Volume Control with Hand", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
