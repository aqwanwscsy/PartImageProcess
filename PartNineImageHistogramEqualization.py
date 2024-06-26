import cv2

# 读取图像
img = cv2.imread("course_01/lenna.jpg")

"""
attention:cv2.equalizeHist()仅适用于单通道(灰度图像)
如果为彩图需要分别处理每个通道，或者将图像转换为 YUV 颜色空间，均衡化亮度通道后再转换回 RGB 颜色空间。
测试的时候适用的是彩图,灰度图的我注释掉了,在下面
"""
# 将图像从 BGR 转换为 YUV
yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
# 对 Y 通道（亮度）进行直方图均衡化
yuv_img[:, :, 0] = cv2.equalizeHist(yuv_img[:, :, 0])
# 将图像从 YUV 转换回 BGR
equalized_image = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2BGR)


#灰度图
# equalized_image = cv2.equalizeHist(img)


cv2.imshow("image",img)
cv2.imshow("Equalized Image", equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()