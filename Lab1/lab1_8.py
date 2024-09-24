import cv2

url = 'http://10.131.137.231:8080/video'
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    cv2.imshow('Task 9', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
