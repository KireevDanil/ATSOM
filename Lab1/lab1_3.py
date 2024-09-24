import cv2

cap = cv2.VideoCapture(r'C:\Users\374\Desktop\file_atsom\video_car.mp4', cv2.CAP_ANY)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)  # Частота кадров

output_path = r'C:\Users\374\Desktop\file_atsom\output_video_car.mp4'

# Выбор кодека и создание объекта записи
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Кодек XVID (для AVI файлов)
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
while True:
    ret, frame = cap.read()  # Захват кадра с видео
    resized = cv2.resize(frame, (640, 480))
    if not ret:
        break  # Прерывание цикла, если кадр не был захвачен

    out.write(frame) #запись в другой файл

    cv2.imshow('video', resized)  # Отображение кадра
    if cv2.waitKey(1) & 0xFF == 27:  # Нажатие клавиши 'Esc'
        break  # Прерывание цикла
print("Видео записано в другой файл")