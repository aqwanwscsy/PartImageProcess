# 读取输入图像
import cv2

image = cv2.imread('course_01/lenna.jpg')

image = cv2.resize(image, (1000,1000))

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()