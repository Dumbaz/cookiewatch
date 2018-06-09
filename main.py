#!/usr/bin/env python3

'''Retrieve all the cookies set by a website'''
___author___ = "www.github.com/Dumbaz"
___status___ = "Development"

from get_cookies import get_website_with_cookies

def main():
	url = "http://www.bing.com"
	#url = "http://www.dotasource.de"
	#url = "https://stackoverflow.com/questions/23110383/how-to-dynamically-build-a-json-object-with-python"

	#print(get_website_with_cookies(url))

	testclass = get_website_with_cookies(url)
	print(testclass.returnJSON())

#for entry in domains_list:
#	get_cookies(entry)


if __name__ == '__main__':
	main()
