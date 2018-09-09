# -*- coding:utf-8 -*-
# Author : xuan
# Date : 2018/9/9 8:51

# from PIL import Image
# src = Image.open("D:\\nvshen.jpg").convert("L")

# 读取文件列表下的图片并转成JPEG格式
# from PIL import Image
# import os
# fileList = os.listdir("D://nvshen")
# for inFile in fileList:
#     outFile = os.path.splitext(inFile)[0] + ".png"
#     if inFile != outFile:
#         try:
#             Image.open("D://nvshen//" + inFile).save(outFile)
#             print inFile
#         except IOError:
#             print "can't convert", inFile
# from PIL import  Image
# src = Image.open("D://nvshen.jpg")
# src.save("D://nvshen.png")

# from PIL import Image
# from pylab import *
# src = Image.open("D://nvshen.jpg")
# imshow(src)
# axis("off")
# show()

# from PIL import Image
# from pylab import *
# # import os
# # def get_imlist(path):
# #     """返回目录中所有JPG图像的文件名列表"""
# #     return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
# # print get_imlist('D://nvshen')

# from PIL import Image
# from pylab import *
# src = Image.open("D://nvshen//april.jpg")
# src = src.convert("L")
# imshow(src)
# show()






# from PIL import Image
# from pylab import *
# src = Image.open("D://nvshen//april.jpg")
# # src.thumbnail((128, 128))
# src.convert('L')
# src.save("april.jpg")
# imshow(src)
# show()

# from PIL import Image
# from pylab import *
# src = Image.open("D://nvshen.jpg")
# # box = (10, 10, 40, 40)
# # region = src.crop(box)
# # region = region.transpose(Image.ROTATE_180) # 逆时针旋转180度
# # src.paste(region, box)
#
# imshow(src)
# show()
# from PIL import Image
# from pylab import *
#
# im = array(Image.open("D://nvshen//april.jpg"))
# imshow(im)
# x = [100, 100, 400, 400]
# y = [200, 500, 200, 500]
# plot(x, y)
# # plot(x[:2], y[:2])
# title("april")
# axis("off")
# show()
from PIL import Image
from pylab import *

im = array(Image.open("D://nvshen.jpg").convert("L"))
figure()
gray()
contour(im, origin='image')
axis('equal')
axis('off')
figure()
hist(im.flatten(), 128)
show()



