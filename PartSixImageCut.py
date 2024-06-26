import cv2

# 读取图像
img = cv2.imread('course_01/lenna.jpg')

# 裁剪图像的区域
crop = img[10:200, 10:204]

# 显示原始图像和裁剪后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Region', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
