#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import time
import os
import urllib
import ImageFile

def PrintLink(bas, abc, part1, part2, part3):
	href = bas
	ImgName = "images/"
	i = 0
	while i < 2:
		href += abc[part1[i]]
		ImgName += abc[part1[i]]
		i += 1

	href += "/"
	ImgName += "-"
	i = 0
	while i < 10:
		href += abc[part2[i]]
		ImgName += abc[part2[i]]
		i += 1

	href += abc[part3]
	ImgName += abc[part3]
	href += ".jpg"
	ImgName += ".jpg"
	if GetSize(href) > 82:
		LoadImg(href, ImgName)
		print(href + " => " + ImgName)
	else:
		print(href + " - Bad image")

def NumIncrement(el, pos, bas):
	while True:
		el[pos] += 1
		if el[pos] >= bas and pos > 0:
			el[pos] = 0
			pos -= 1
		else:
			break
	return el

def LoadImg(href, name):
	resource = urllib.urlopen(href)
	out = open(name, 'wb')
	#print(os.path.getsize(resource.read()))
	out.write(resource.read())
	out.close()

def GetSize(uri):
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
	return size



alphabet = ['0', '1', '2', '3',
'4', '5', '6', '7',
'8', '9', '_', '-',
'A', 'B', 'C', 'D',
'E', 'F', 'G', 'H',
'I', 'G', 'K', 'L',
'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T',
'U', 'V', 'W', 'X',
'Y', 'Z', 'a', 'b',
'c', 'd', 'e', 'f',
'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r',
's', 't', 'u', 'v',
'w', 'x', 'y', 'z']

base = 64

#print("Input any image VK link")
href = sys.stdin.readline()
basic = href[:39]

el1 = [0, 0]
#el2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#el3 = 0

#PrintLink(basic, el1, el2, el3)

cnt = 0
while el1[0] < base:
	el2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	while el2[0] < base:
		el3 = 0
		while el3 < base:
			ImgName = PrintLink(basic, alphabet, el1, el2, el3)
			time.sleep(1)
			#print(el1, el2, el3)
			el3 += 4
			cnt += 1
			if cnt > 300:
				cnt = 0
				time.sleep(30)
		NumIncrement(el2, 9, base)
	NumIncrement(el1, 1, base)
