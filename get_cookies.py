#!/usr/bin/env python3

'''Retrieve all the cookies set by a website'''
___author___ = "www.github.com/Dumbaz"
___status___ = "Development"

import requests
import json


class Website_information(object):
	"""
	Contains the website URL, and a list of cookies.
	List of Cookies can be empty 
	Can be serialized to JSON, as we want to export to Elasticsearch
	"""
	def __init__(self, url, cookies):
		super(Website_information, self).__init__()
		self.url = url
		self.cookies = cookies
		self.sslError = False
		self.connectionTimeout = False
		self.readTimeout = False
		self.excessiveRedirects = False
	def hasCookies(self):
		if len(self.cookies) == 0:
			return False
		else:
			return True
	def countCookies(self):
		return len(self.cookies)
	def returnCookies(self):
		return self.cookies
	def returnJSON(self):
		data = {}
		data['url'] = self.url
		cookieslist = {}
		for cookie in self.cookies:
			cookieslist[cookie.name] = cookie.__dict__
		data['cookies'] = cookieslist
		return json.dumps(data)


def get_website_with_cookies(url):
	thisclass = Website_information(url, [])
	try:
		r = requests.get(url, timeout=5)
		if r.status_code == 200:
			for cookie in r.cookies:
				thisclass.cookies.append(cookie)
	except requests.exceptions.SSLError:
		# Mismatch between www.domain and domain
		thisclass.sslError = True
	except requests.exceptions.ConnectionError:
		thisclass.connectionTimeout = True
	except requests.exceptions.ReadTimeout:
		thisclass.readTimeout = True
	except requests.exceptions.TooManyRedirects:
		thisclass.excessiveRedirects = True
	return thisclass
