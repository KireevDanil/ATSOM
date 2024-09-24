import cv2
import numpy as np

# Захват видеопотока с веб-камеры
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Чтение кадра с веб-камеры
    if not ret:
        break

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    rect_width = width // 30
    rect_height = height // 8

    # Центр изображения
    center_x = width // 2
    center_y = height // 2

    # Параметры вертикального прямоугольника (по центру вертикально)
    vert_rect_top_left = (center_x - rect_width // 2, center_y - rect_height)  # Верхняя левая точка
    vert_rect_bottom_right = (center_x + rect_width // 2, center_y + rect_height)  # Нижняя правая точка

    # Параметры горизонтального прямоугольника (по центру горизонтально)
    horiz_rect_top_left = (center_x - rect_height, center_y - rect_width // 2)  # Верхняя левая точка
    horiz_rect_bottom_right = (center_x + rect_height, center_y + rect_width // 2)  # Нижняя правая точка

    # Получение значения центрального пикселя (в формате BGR)
    central_pixel = frame[center_y, center_x]
    blue, green, red = central_pixel

    # Создание маски на основе максимального значения центрального пикселя
    mask_color = [0, 0, 0]  # Изначально все компоненты равны 0
    max_value = max(blue, green, red)

    # Определение компонента с максимальным значением
    if max_value == blue:
        mask_color = [255, 0, 0]  # Синий
    elif max_value == green:
        mask_color = [0, 255, 0]  # Зелёный
    elif max_value == red:
        mask_color = [0, 0, 255]  # Красный


    cv2.rectangle(frame, vert_rect_top_left, vert_rect_bottom_right, mask_color, -1)
    cv2.rectangle(frame, horiz_rect_top_left, horiz_rect_bottom_right, mask_color, -1)

    # Отображение кадра с крестом
    cv2.imshow('Filling in the cross', frame)

    # Прерывание при нажатии клавиши 'Esc'
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
