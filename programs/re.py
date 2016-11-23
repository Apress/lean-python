from __future__ import print_function
import httplib    # the library to download web pages
import re         # The RegEx library
#
#   this code opens a connection to the leanpy.com website
#
conn = httplib.HTTPConnection("leanpy.com")
conn.request("GET", "/")
r1 = conn.getresponse()     # get the home page text
print(r1.status, r1.reason) # print the status and message
data1 = r1.read()           # put response text in data
#
#   our regular expression (to find links)
#
regex = '<a\s[^>]*href\s*=\s*\"([^\"]*)\"[^>]*>(.*?)</a>'
#
#   compile the regex and perform the match (find all)
#
pm = re.compile(regex)
matches = pm.findall(data1)
#
#   matches is a list
#   m[0] - the url of the link
#   m[1] - text associated with the link
#
for m in matches:
    ms=''.join(('Link: "',m[0],'" Text: "',m[1],'"'))
    print(ms)

conn.close()
