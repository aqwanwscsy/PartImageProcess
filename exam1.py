import cv2
import numpy as np

# 读取图像
img = cv2.imread("img/ceels1.jpg")

# 提取红色通道
red_channel = img[:, :, 2]  # OpenCV中通道顺序为BGR，0为蓝色通道，1为绿色通道，2为红色通道

# 计算均值、中位数和标准差
mean_value = np.mean(red_channel)
median_value = np.median(red_channel)
std_deviation = np.std(red_channel)

# 打印结果
print(f"红色通道的均值: {mean_value}")
print(f"红色通道的中位数: {median_value}")
print(f"红色通道的标准差: {std_deviation}")
