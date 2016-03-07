#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import urllib2
import ImageFile

def _fetch_image(url):
	"""Return the image by URL downloading as little as possible."""

	user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
	request = urllib2.Request(url)
	request.add_header('User-Agent', user_agent)
	parser = ImageFile.Parser()
	response = None
	try:
		response = urllib2.urlopen(request)
		while True:
			chunk = response.read(1024)
		if not chunk:
			sys.exit()
		parser.feed(chunk)
		if parser.image:
			return parser.image
	except:
		return None
	finally:
		if response:
			response.close()

src = 'https://pp.vk.me/c633920/v633920933/19700/000000PCMfY.jpg'
print(_fetch_image(src))
