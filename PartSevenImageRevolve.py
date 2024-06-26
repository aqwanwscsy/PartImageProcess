

'''

'''
# import cv2
# import numpy as np
# img =cv2.imread("course_01/lenna.jpg")
# img = np.rot90(img, 10)
#
# cv2.imshow('Original Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
上面的有点垃圾我注释掉了,他只能旋转90或者180
可以用下面这个或者后面的仿射变换PartEight
'''

import cv2
import numpy as np
from scipy.ndimage import rotate

# 读取图像
img = cv2.imread("course_01/lenna.jpg")

# 使用 SciPy 进行任意角度旋转
angle = 45  # 旋转角度
rotated_img = rotate(img, angle, reshape=True)

# 将旋转后的图像转换为适合显示的格式（0-255的范围）
rotated_img = np.clip(rotated_img, 0, 255).astype(np.uint8)

# 显示原始图像和旋转后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()