
import cv2

img = cv2.imread('course_01/lenna.jpg')


cv2.imshow('Original', img)

"""
blurred_image = cv2.GaussianBlur(src, ksize, sigmaX, sigmaY = None, borderType = None)
src：输入图像，即要进行模糊处理的图像，通常是一个多通道图像。
ksize：高斯内核的大小。它是一个 (width, height) 的元组，表示高斯核的宽度和高度。这两个值必须是正奇数。例如，(5, 5) 表示一个 5x5 的高斯核。
sigmaX：X 方向上的标准差（即水平方向）。如果设为 0，则根据 ksize 自动计算。
sigmaY：Y 方向上的标准差（即垂直方向）。如果未指定，则默认与 sigmaX 相同。通常情况下，如果只指定 sigmaX，则 sigmaY 也会自动设为相同的值。
borderType：边界模式。这是可选参数，用于指定在处理边界像素时的行为。默认为 cv2.BORDER_DEFAULT。
"""

blur_image = cv2.GaussianBlur(img, (5, 5), 0)  # (5, 5)表示高斯矩阵的长与宽都是5，标准差取0
cv2.imshow('Blurred Image', blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
