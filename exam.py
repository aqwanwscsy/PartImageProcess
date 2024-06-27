import cv2

# 读取图像
img = cv2.imread("img/ceels1.jpg")

# 定义裁剪区域的坐标
x1, y1 = 162, 38
x2, y2 = 204, 70

# 裁剪图像
cropped_img = img[y1:y2, x1:x2]

# 获取裁剪后图像的尺寸
height, width, channels = cropped_img.shape

# 将图像放大两倍
scaled_img = cv2.resize(cropped_img, (2*width, 2*height))

# 显示原始图像和放大后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Scaled Image', scaled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
