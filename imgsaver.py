#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

def PrintLink(bas, abc, part1, part2, part3):
	out = bas
	i = 0
	while i < 2:
		out += abc[part1[i]]
		i += 1

	out += "/"
	i = 0
	while i < 10:
		out += abc[part2[i]]
		i += 1

	out += abc[part3]
	out += ".jpg"
	print(out)

def NumIncrement(el, pos, bas):
	while True:
		el[pos] += 1
		if el[pos] >= bas and pos > 0:
			el[pos] = 0
			pos -= 1
		else:
			break
	return el

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

while el1[0] < base:
	el2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	while el2[0] < base:
		el3 = 0
		while el3 < base:
			PrintLink(basic, alphabet, el1, el2, el3)
			#print(el1, el2, el3)
			el3 += 4
		NumIncrement(el2, 9, base)
	NumIncrement(el1, 1, base)
