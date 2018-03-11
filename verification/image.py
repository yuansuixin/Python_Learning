from captcha.image import ImageCaptcha
import random

# 生成验证码
# write函数有3个参数，第一个指定要生成的文本，第二个参数是指定输出的位置，
# 第三个参数是指定生成图片的格式
# image = ImageCaptcha()
# ImageCaptcha类的初始化方法有width，height，fonts和font_size四个可选参数，
# 分别指定验证码的宽高，字体和字体的尺寸
# image.write('Fishc','captcha2.png')
# # 大写字母65-91
# upper = chr(random.randrange(65, 91))
# # 小写字母97-123
# lower = chr(random.randrange(97, 123))
# # 数字48-58
# num = chr(random.randrange(48, 58))
# print(upper, lower, num)

verification_code = ''
# 使用1,2,3分别代表大小写字母和数字，随机生成1-3这3个数字，来随机生成6位验证码
for i in range(1, 7):
    n = i % 3
    if n == 1:
        m = chr(random.randrange(65, 91))
    elif n == 2:
        m = chr(random.randrange(97, 123))
    elif n == 0:
        m = str(chr(random.randrange(48, 58)))
    verification_code += m
print(verification_code)
image = ImageCaptcha()
image.write(verification_code,'verification.png')
