#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#Здесь скачивается изображение по заданной ссылке

import urllib

img = "http://www.fortrainz.ru/load/objects/tpt-pak-budok/logo.jpg"
resource = urllib.urlopen(img)
out = open("img.jpg", 'wb')
out.write(resource.read())
out.close()