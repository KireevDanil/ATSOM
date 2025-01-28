import cv2
import numpy as np

cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()
    if not ret:
        print("Не удалось захватить изображение с камеры")
        break

    # Переводим изображение в формат HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 40, 200])
    upper_red1 = np.array([20, 180, 255])

    lower_red2 = np.array([170, 40, 200])
    upper_red2 = np.array([180, 180, 255])

    mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)

    # Комбинируем маски
    mask = mask1 + mask2
    # Применяем маску к оригинальному изображению
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
