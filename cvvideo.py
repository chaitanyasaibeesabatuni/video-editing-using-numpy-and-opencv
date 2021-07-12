
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    video=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    zeros = np.zeros(frame.shape, dtype="uint8")
    b, g, r = cv2.split(frame)
    blue = cv2.merge([b, zeros, zeros])
    green = cv2.merge([zeros, g, zeros])
    red = cv2.merge([zeros, zeros, r])

    cv2.imshow('image_blue', b[2:])
    cv2.imshow('image_green ', g[2:])
    cv2.imshow('image_red ', r[20:])

    cv2.imshow('frame',frame[20:])
    cv2.imshow('gray',gray[20:])
    cv2.imshow('rgb', video[20:])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()