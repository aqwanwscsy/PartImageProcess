import cv2

# 读取输入图像
image = cv2.imread('course_01/lenna.jpg')

# 水印文字
watermark_txt = 'I LOVE YOU'

# 设置字体、位置、字体缩放比例、颜色和粗细
font = cv2.FONT_HERSHEY_SIMPLEX
position = (50, 50)
font_scale = 2
color = (255, 0, 0)  # 白色
thickness = 2

'''
原理:创建一个叠加层图片,然后两个图片叠加
'''

# 创建叠加层
overlay = image.copy()

# 在叠加层上添加文字
cv2.putText(overlay, watermark_txt, position, font, font_scale, color, thickness)

# 合并图像
combined = cv2.addWeighted(image, 0.7, overlay, 0.3, 0)

# 显示结果
cv2.imshow('Combined Image', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
