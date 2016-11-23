from __future__ import print_function
import httplib    # the library to download web pages
#
#   this code opens a connection to the leanpy.com website
#
url=raw_input('Enter website url:')
conn = httplib.HTTPConnection(url)
conn.request("GET", "/")
r1 = conn.getresponse()     # get the home page text
print(r1.status, r1.reason) # print the status and message
text = r1.read()           # put response text in data

print(text)
