import cv2

# 提取对应颜色通道,求对应通道所有像素点的均值

image = cv2.imread('course_01/lenna.jpg')

# 蓝色通道
blue_channel = image[:, :, 0]
# 绿色通道
green_channel = image[:, :, 1]
# 红色通道
red_channel = image[:, :, 2]

mean_blue = blue_channel.mean()
mean_green = green_channel.mean()
mean_red = red_channel.mean()

print(mean_blue)
print(mean_red)
print(mean_green)
