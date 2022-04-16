"""
纯粹的turtle图像生成器，目的是在于可以导入图片，并且生成相应的turtle绘制代码
经过测试，大于50*50像素的turtle文件画图速度非常慢，个人看来50**2的图像大小是经过妥协后的最佳选择了
生成代码文件需要约5分钟左右，需要慢慢等待
并且，生成的文件需要手动进行导入包操作，并且导入turtle为tt
"""


from PIL import Image
import numpy as np
"""
import turtle as tt
tt.Screen().colormode(255)
tt.setup(500, 500)
tt.pensize(10)
"""
image = Image.open(r'1.jpg').convert('RGB')  # 读取图片,名称为1.jpg并且大小为50*50左
print(image)
print(image.size)
image_array_RGB = np.asarray(image)  # 产生二维数组，存储xy对应的RGB值
# tt.speed(0) 乌龟绘画速度达到最快水平
TheText = open('Code.txt', 'w')  # 创建txt文件存储生成的源码
for x in range(48): # 图像长度
    a = image_array_RGB[x]
    # tt.penup()
    for y in range(50): # 图像宽度
        b = a[y]
        R = int(b[0])
        G = int(b[1])
        B = int(b[2])  # 读取像素RGB值
        """
        tt.pencolor(R, G, B)
        tt.goto(-250 + y * 10, 250 - x * 10)
        tt.pd()
        tt.fd(10)
        tt.penup()
        """
        # 写入txt文件的内容
        TheText.write('tt.pencolor(' + str(R) + ',' + str(G) + ',' + str(B) + ')\n')  # 笔刷颜色设置
        TheText.write('tt.goto(' + str(-250 + y * 10) + ',' + str(250 - x * 10) + ')\n')  # 笔刷位置设置
        TheText.write('tt.pd()\n')
        TheText.write('tt.fd(10)\n')
        TheText.write('tt.penup()\n')
# tt.penup()
# tt.done()
print("OK")
