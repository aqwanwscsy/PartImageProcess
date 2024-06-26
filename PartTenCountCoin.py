import cv2
import numpy as np

# 读取彩色图像
color_img = cv2.imread('img/cells.jpg')



"""
调参数适应形状
cv2.GaussianBlur(gray_img, (9, 9), 2)的ksize(必须是正奇数)和sigmaX高斯核在 X 方向的标准偏差。
如果设置为 0，则根据内核大小自动计算。
cv2.threshold(gray_img, 80, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)的thresh阈值
ones((5, 5), np.uint8)的shape 这个不怎么改
erode(thresh, kernel, iterations = 3)的iterations
 if area > 1 :  # 只考虑面积大于5的轮廓 这里设置一下大小
"""

# 将图像转换为灰度图像
gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('test', gray_img)
# cv2.waitKey(0)

'''attention:这里是灰度反转,如果需要数的全部变白了可以用'''
gray_img = 255 - gray_img



# 对灰度图像进行高斯模糊
gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

# 使用Otsu阈值化方法进行二值化
_, thresh = cv2.threshold(gray_img, 80, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 创建一个5x5的核进行膨胀操作
kernel = np.ones((5, 5), np.uint8)

# 对二值图像进行膨胀操作
dilated_img = cv2.erode(thresh, kernel, iterations = 0)

# 显示膨胀后的图像
cv2.imshow('Dilated Image', dilated_img)
cv2.waitKey(0)

# 查找图像中的轮廓
contours, _ = cv2.findContours(dilated_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 初始化计数器
cell_count = 0

# 拷贝原始图像，用于标记
marked_img = color_img.copy()

# 遍历每一个轮廓
for i, cnt in enumerate(contours):
    area = cv2.contourArea(cnt)

    x, y, w, h = cv2.boundingRect(cnt)

    # 根据面积和形状过滤掉方形干扰物（例如，面积大于某个阈值且长宽比接近1的轮廓）
    aspect_ratio = float(w) / h
    if area > 260 :  # 只考虑面积大于5的轮廓
        cell_count += 1
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(marked_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(marked_img, str(cell_count), (x + 7, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# 打印细胞数量
print("cell_count:", cell_count)

# 显示标记后的图像
cv2.imshow('Marked Image', marked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
