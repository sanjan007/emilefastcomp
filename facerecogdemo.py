import cv2
import sys


whatwewantinaface = cv2.CascadeClassifier("C:\pythonProject3\modules\haarcascade_frontalface_default.xml")
recordvideoforprogram = cv2.VideoCapture(0)

while True:


    eachFrame, frame = recordvideoforprogram.read()
    frame=cv2.flip(frame, 1, 0)
    colorgrayforscan = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facesintheroom = whatwewantinaface.detectMultiScale(
        colorgrayforscan,
        scaleFactor=1.1,
        minNeighbors=6,
        minSize=(35, 35)
    )
    numberoffaces = int(len(facesintheroom))

    for (axisx, axisy, coordinw, coordinh) in facesintheroom:
        cv2.rectangle(frame, (axisx, axisy), (axisx + coordinw, axisy + coordinh), (0, 255, 0), 2)


    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('l'):
       sys.exit()