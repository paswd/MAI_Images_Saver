#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#Просто функция. Использовать внутри других программ

def move(letter):
    if letter.lower()=='z':
        return unichr(97)
    return unichr(ord(letter.lower())+1)