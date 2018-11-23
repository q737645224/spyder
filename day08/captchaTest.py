# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:52:17 2018

@author: Python
"""

from PIL import Image
import random
import numpy as np#做矩阵运算的库
from captcha.image import ImageCaptcha


number = ['0','1','2','3','4','5','6','7','8','9']
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ALPHABET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def random_captcha_text(char_set=number+alphabet+ALPHABET, 
                        captcha_size=4):
    """
    随机生成一个包含四个字母或者数字的信息
    """
    captcha_text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text

def gen_captcha_text_and_image():
   """
   随机得到一个包含有4个字符的验证码图片和字符集
   """
   image = ImageCaptcha()
   
   # 调用生成组合
   captcha_text = random_captcha_text()
   # 把得到的list改造成字符串，以便于生产字符验证码
   captcha_text = ''.join(captcha_text)
   #print(captcha_text)
   capthcaInfo = image.generate(captcha_text)
   
   #生成验证码图片 
   captcha_image = Image.open(capthcaInfo)
   captcha_image = np.array(captcha_image)
   im = Image.fromarray(captcha_image)
   im.save("captcha.png")
   
   return captcha_text,captcha_image

#print(random_captcha_text())
#print(random_captcha_text())
gen_captcha_text_and_image()
    
    
    
    
    
    
    
    
    
    
    
    
    