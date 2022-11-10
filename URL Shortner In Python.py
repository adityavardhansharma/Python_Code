pip install pyshorteners

import pyshorteners
long_url = input("Enter the Url to shorten: ")
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
print("The Short Url is: " + short_url)