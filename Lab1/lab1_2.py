import cv2

cap = cv2.VideoCapture(r'C:\Users\374\Desktop\file_atsom\video_car.mp4', cv2.CAP_ANY)

while True:
    ret, frame = cap.read()  # Захват кадра с видео
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    resized = cv2.resize(frame, (640, 480))
    if not ret:
        break  # Прерывание цикла, если кадр не был захвачен
    cv2.imshow('video', resized)  # Отображение кадра
    if cv2.waitKey(1) & 0xFF == 27:  # Нажатие клавиши 'Esc'
        break  # Прерывание цикла
