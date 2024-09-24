import cv2

img_jpg = cv2.imread(r'C:\Users\374\Desktop\file_atsom\image_jpg.jpg',cv2.IMREAD_UNCHANGED)
hsv = cv2.cvtColor(img_jpg, cv2.COLOR_BGR2HSV)

cv2.namedWindow('JPG', cv2.WINDOW_NORMAL)
cv2.namedWindow('JPG_HSV', cv2.WINDOW_NORMAL)

cv2.resizeWindow('JPG',640,600)
cv2.resizeWindow('JPG_HSV',640,600)

cv2.imshow('JPG', img_jpg)
cv2.imshow('JPG_HSV', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
