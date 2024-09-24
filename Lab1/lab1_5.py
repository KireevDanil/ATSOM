import cv2

# Открытие видеопотока с камеры
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Ошибка открытия камеры")
else:
    while True:
        ret, frame = cap.read()  # Чтение кадра с камеры
        if not ret:
            break

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        rect_width = width // 20
        rect_height = height // 4

        # Центр изображения
        center_x = width // 2
        center_y = height // 2

        # Параметры вертикального прямоугольника (по центру вертикально)
        vert_rect_top_left = (center_x - rect_width // 2, center_y - rect_height)  # Верхняя левая точка
        vert_rect_bottom_right = (center_x + rect_width // 2, center_y + rect_height)  # Нижняя правая точка
        vert_rect_color = (0, 0, 255)

        # Параметры горизонтального прямоугольника (по центру горизонтально)
        horiz_rect_top_left = (center_x - rect_height, center_y - rect_width // 2)  # Верхняя левая точка
        horiz_rect_bottom_right = (center_x + rect_height, center_y + rect_width // 2)  # Нижняя правая точка
        horiz_rect_color = (0, 0, 255)

        # Извлечение области вертикального прямоугольника
        rect_blur = frame[horiz_rect_top_left[1]:horiz_rect_bottom_right[1], horiz_rect_top_left[0]:horiz_rect_bottom_right[0]]
        print(rect_blur)
        # Применение размытия к этой области
        blurred_rect = cv2.GaussianBlur(rect_blur, (15, 15), 0)  # Размытие Гаусса

        # Замена области на размытый прямоугольник
        frame[horiz_rect_top_left[1]:horiz_rect_bottom_right[1], horiz_rect_top_left[0]:horiz_rect_bottom_right[0]] = blurred_rect

        cv2.rectangle(frame, vert_rect_top_left, vert_rect_bottom_right, vert_rect_color, 2)
        cv2.rectangle(frame, horiz_rect_top_left, horiz_rect_bottom_right, horiz_rect_color, 2)

        cv2.imshow('Cross', frame)

        # Остановка при нажатии клавиши 'Esc'
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Освобождение ресурсов камеры
    cap.release()
    cv2.destroyAllWindows()