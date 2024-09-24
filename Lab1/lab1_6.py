import cv2


cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(r'C:\Users\374\Desktop\file_atsom\out_web.mp4', fourcc, 20, (640, 480))

while True:
    ret, frame = cap.read()  # Чтение кадра с веб-камеры
    if not ret:
        print("Не удалось захватить кадр")
        break
    cv2.imshow('Recording video on webcam', frame)
    # Запись кадра в файл
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Освобождение ресурсов
cap.release()
out.release()
cv2.destroyAllWindows()