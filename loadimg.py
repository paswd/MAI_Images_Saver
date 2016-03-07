#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#Здесь скачивается изображение по заданной ссылке

import urllib
import os

img = "https://pp.vk.me/c633920/v633920933/19700/000000PCMfY.jpg"
resource = urllib.urlopen(img)
out = open("img3.jpg", 'wb')
print(os.path.getsize(resource.read()))
out.write(resource.read())
out.close()