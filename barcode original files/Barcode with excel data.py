import cv2
from pyzbar.pyzbar import decode
import time
import openpyxl
cap = cv2.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 600)
used_codes = []
workbook = openpyxl.Workbook()
workspace = workbook.active
camera = True
while camera:
    success, frame = cap.read()
    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print("approved👍👍👍you can enter your vote!! ")
            print(code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(2)
            workspace.append([code.data.decode('utf-8')])
        elif code.data.decode('utf-8') in used_codes:
            print("Sorry🚫this card has been already voted❌❌❌")
            time.sleep(2)
        else:
            pass
    workbook.save("barcode data .xlsx")
    cv2.imshow('testing-code-scan', frame)
    cv2.waitKey(1)
    