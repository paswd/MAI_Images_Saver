#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import ImageFile

def getsizes(uri):
    # get file size *and* image size (None if not known)
    file = urllib.urlopen(uri)
    size = file.headers.get("content-length")
    if size: size = int(size)
    p = ImageFile.Parser()
    while 1:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return size
            #return size, p.image.size
            break
    file.close()
    return size, None

print getsizes("https://pp.vk.me/c633920/v633920933/19700/000000PCMfY.jpg")
