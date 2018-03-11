from captcha.image import ImageCaptcha

# 生成图片验证码
# image = ImageCaptcha(fonts=['data/SIMYOU.TTF','data/STSONG.TTF'])
# image.write('Fishc','captcha1.png')

# 生成音频验证码
from captcha.audio import AudioCaptcha

audio = AudioCaptcha(voicedir='data/') # 指定声音素材
audio.write('1024','captcha.wav')





