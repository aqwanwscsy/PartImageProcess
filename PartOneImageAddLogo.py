import cv2

# 读取输入图像和水印图像
# 换成自己存放图片的位置
image = cv2.imread('course_01/lenna.jpg')
watermark = cv2.imread('img/GoogleLogo.jpg')

'''
判断图像尺寸是否相同，如果不同的话，将logo的尺寸放大或缩小为图像的尺寸
attention:resize中的参数是(img,(width,height)),而不是(img.(height,width))
'''
# 检查图像尺寸
if image.shape[:2] != watermark.shape[:2]:
    # 调整水印图像的尺寸
    watermark = cv2.resize(watermark, (image.shape[1], image.shape[0]))
# '''
# 修改尺寸也可以这样写
# '''
# h_i, w_i = image.shape[:2]
# h_m, w_m = watermark.shape[:2]
# if h_i != h_m or w_i != w_m:
#     # 调整尺寸
#     watermark = cv2.resize(watermark, (w_i, h_i))


# 检查通道数,通道数不同会报错,所以加一个检查通道,这个不写也没关系
if len(image.shape) == 3 and len(watermark.shape) == 2:
    # 如果输入图像是彩色图像而水印是灰度图像
    watermark = cv2.cvtColor(watermark, cv2.COLOR_GRAY2BGR)
elif len(image.shape) == 2 and len(watermark.shape) == 3:
    # 如果输入图像是灰度图像而水印是彩色图像
    watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2GRAY)



# 合并图像
# 参数分析解释：cv2.addWeighted(image,img的权重,logo,logo的权重,img和logo做和后添加的数值，小一点)
combined = cv2.addWeighted(image, 0.7, watermark, 0.3, 0)

# 显示结果
cv2.imshow('Combined Image', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

