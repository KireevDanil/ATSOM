import cv2
import numpy as np


#Задание 1

def build_a_Gaussian_matrix():

    kernel_sizes = [3,5,7] #размер ядра
    deviation = 3 #отклонение
    for k_size in kernel_sizes:
        kernel = np.zeros((k_size,k_size))
        a = b = k_size//2 #математическое ожидание - координаты центрального пикселя ядра
        for i in range(k_size):
            for j in range(k_size):
                kernel[i,j] = gauss_func(deviation,a,b,i,j)

        print("Отклонение: ", deviation)
        print("Размерность: ", k_size)
        print("Ядро: ", kernel)
        print()


#Функция Гаусса
def gauss_func(deviation,a,b,x,y):
        m1 = 1 / (2 * np.pi * (deviation**2))
        m2 = np.exp(-((x - a) ** 2 + (y - b) ** 2) / (2*(deviation**2)))

        return m1 * m2



#Задание 2
def Normalize_the_resulting_Gaussian_matrix():
    kernel_sizes = [3, 5, 7]  # размер ядра
    deviation = 3  # отклонение
    for k_size in kernel_sizes:
        kernel = np.zeros((k_size, k_size))
        a = b = k_size // 2  # математическое ожидание - координаты центрального пикселя ядра
        for i in range(k_size):
            for j in range(k_size):
                kernel[i, j] = gauss_func(deviation, a, b, i, j)

        print("Отклонение: ", deviation)
        print("Размерность: ", k_size)
        print("Ядро до нормализации: ", kernel)

        # нормализуем для сохранения яркости изображения
        sum = 0
        for i in range(k_size):
            for j in range(k_size):
                sum += kernel[i, j]

        for i in range(k_size):
            for j in range(k_size):
                kernel[i, j] /= sum

        print("Ядро после нормализации: ",kernel)
        print()

#Задание 3 фильтр Гаусса
def GaussBlur(img,k_size,deviation):

    height, width = img.shape[0],img.shape[1]

    kernel = np.zeros((k_size, k_size))
    a = b = k_size // 2  # математическое ожидание - координаты центрального пикселя ядра
    for i in range(k_size):
        for j in range(k_size):
            kernel[i, j] = gauss_func(deviation, a, b, i, j)

    print("Отклонение: ", deviation)
    print("Размерность: ", k_size)
    print("Ядро до нормализации: ", kernel)

    # нормализуем для сохранения яркости изображения
    sum = 0
    for i in range(k_size):
        for j in range(k_size):
            sum += kernel[i, j]

    for i in range(k_size):
        for j in range(k_size):
            kernel[i, j] /= sum

    print("Ядро после нормализации: ",kernel)

    blured_img = img.copy()

    #применяем фильтр к пикселям картинки
    for x in range(k_size//2,height-k_size//2):
        for y in range(k_size//2,width-k_size//2):
            # свертка
            val = 0
            for k in range(-(k_size // 2), k_size // 2 + 1):
                for l in range(-(k_size // 2), k_size // 2 + 1):
                    val += img[x + k, y + l] * kernel[k + (k_size // 2), l + (k_size // 2)]
            blured_img[x, y] = val
    return blured_img


#Задание 4
def GaussBlurCompareValues():
    img = cv2.imread('bike.jpg', 0)
    if img is None:
        print("Ошибка: изображение не загружено.")
        return

    height, width = img.shape

    kernel_sizes = [5, 7]  # Размер ядра
    deviations = [1, 30]    # Отклонение (0 заменен на 1)

    for p in range(len(kernel_sizes)):
        k_size, deviation = kernel_sizes[p], deviations[p]

        # Создание ядра
        kernel = np.zeros((k_size, k_size), dtype=np.float32)
        a = b = k_size // 2
        for i in range(k_size):
            for j in range(k_size):
                kernel[i, j] = gauss_func(deviation, a, b, i, j)

        print(f"Отклонение: {deviation}")
        print(f"Размер ядра: {k_size}")
        print("Ядро до нормализации:\n", kernel)

        # Нормализация ядра
        kernel_sum = np.sum(kernel)
        if kernel_sum > 0:
            kernel /= kernel_sum

        print("Ядро после нормализации:\n", kernel)

        # Применение фильтра
        blured_img = np.zeros_like(img, dtype=np.float32)

        for x in range(k_size // 2, height - k_size // 2):
            for y in range(k_size // 2, width - k_size // 2):
                val = 0
                for k in range(-k_size // 2, k_size // 2 + 1):
                    for l in range(-k_size // 2, k_size // 2 + 1):
                        val += img[x + k, y + l] * kernel[k + k_size // 2, l + k_size // 2]
                blured_img[x, y] = val

        # Приведение к uint8
        blured_img = np.clip(blured_img, 0, 255).astype(np.uint8)

        # Отображение изображений
        cv2.imshow(f'Original (Deviation {deviation})', img)
        cv2.imshow(f'Blurred (Kernel {k_size}, Deviation {deviation})', blured_img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()



#Задание 5
def CompareGaussBlur():
    img = cv2.imread('bike.jpg', 0)
    blur_lib = cv2.GaussianBlur(img, (5, 5), 1)
    blur_mine = GaussBlur(img,5,1)

    cv2.namedWindow('Img', cv2.WINDOW_NORMAL)
    cv2.imshow('Img', img)

    cv2.namedWindow('Blured Img by me', cv2.WINDOW_NORMAL)
    cv2.imshow('Blured Img by me', blur_mine)

    cv2.namedWindow('Blured Img by lib', cv2.WINDOW_NORMAL)
    cv2.imshow("Blured Img by lib", blur_lib)
    cv2.waitKey(0)


CompareGaussBlur()
