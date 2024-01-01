import cv2
from pyzbar.pyzbar import decode
import time
cap = cv2.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 600)
used_codes = []
camera = True
while camera == True:
    success, frame = cap.read()
    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print("approved. you can enter ! ")
            print(code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(5)
        elif code.data.decode('utf-8') in used_codes:
            print("Sorry, this code has been already used")
            time.sleep(5)
        else:
            pass

    cv2.imshow('testing-code-scan',frame)
    cv2.waitKey(1)