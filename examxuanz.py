import cv2
import numpy as np
from scipy.ndimage import rotate

# 读取图像
img = cv2.imread("img/hand.jpg")

# 使用 SciPy 进行任意角度旋转
angle = 40 # 旋转角度
rotated_img = rotate(img, angle, reshape=True)

# 将旋转后的图像转换为适合显示的格式（0-255的范围）
rotated_img = np.clip(rotated_img, 0, 255).astype(np.uint8)

# 显示原始图像和旋转后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = rotated_img
cv.imshow('Cats', img)
cv.waitKey()

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
cv.waitKey()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey()

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
cv.waitKey()

ret, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
cv.waitKey()

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (255,255,255), 1)
blank = 255-blank
cv.imshow('Contours Drawn', blank)
cv.imwrite('111.png',blank)
cv.waitKey(0)
