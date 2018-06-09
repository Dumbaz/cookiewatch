#!/usr/bin/env python3

'''Retrieve all the cookies set by a website'''
___author___ = "www.github.com/Dumbaz"
___status___ = "Development"

import logging
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
		data['cookies'] = []
		for cookie in self.cookies:
			data['cookies'].append(cookie.__dict__)
		return json.dumps(data)



url = "http://www.bing.com"
#url = "http://www.dotasource.de"
url = "https://stackoverflow.com/questions/23110383/how-to-dynamically-build-a-json-object-with-python"


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
		print("SSL Error for URL " + url)
	except requests.exceptions.ConnectionError:
		thisclass.connectionTimeout = True
		print("There seems to be no connection to " + url)
	except requests.exceptions.ReadTimeout:
		thisclass.readTimeout = True
		print("This " + url + " website keeps loading forever")
	except requests.exceptions.TooManyRedirects:
		thisclass.excessiveRedirects = True
		print("These are a lot of redirects on " + url)
	return thisclass

#print(get_website_with_cookies(url))

testclass = get_website_with_cookies(url)
print(testclass.returnJSON())

#for entry in domains_list:
#	get_cookies(entry)