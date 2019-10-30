from PIL import Image

image = Image.open('./res/guido.jpg')
image.format, image.size, image.mode = ('JPEG', (500, 750), 'RGB')
image.show()


# 裁剪图像
image = Image.open('./res/guido.jpg')
rect = 80, 20, 310, 360
image.crop(rect).show()

# 生成缩略图
image = Image.open('./res/guido.jpg')
size = 128, 128
image.thumbnail(size)
image.show()

# 缩放和黏贴图像
image1 = Image.open('./res/luohao.png')
image2 = Image.open('./res/guido.jpg')
rect = 80, 20, 310, 360
guido_head = image2.crop(rect)
width, height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))

# 旋转和翻转
image = Image.open('./res/guido.png')
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()

#  操作像素
image = Image.open('./res/guido.jpg')
for x in range(80, 310):
    for y in range(20, 360):
        image.putpixel((x, y), (128, 128, 128))
image.show()


# 滤镜效果
from PIL import Image, ImageFilter

image = Image.open('./res/guido.jpg')
image.filter(ImageFilter.CONTOUR).show()