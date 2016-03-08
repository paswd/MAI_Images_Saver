#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

def PrintLink(bas, part1, part2, part3):
	out = ""
	for i in el1:
		out += alphabet[el1[i]]

	out += "/"

	for i in el2:
		out += alphabet[el2[i]]

	out += alphabet[el3]
	out += ".jpg"
	print(bas + out)



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

print("Input any image VK link")
href = sys.stdin.readline()
basic = href[:39]

el1 = [0, 0]
el2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
el3 = 0

PrintLink(basic, el1, el2, el3)


#print(href[:39])
#while el1[0] < base:
#	while el2[0] < base:
#		while el3 < base:
