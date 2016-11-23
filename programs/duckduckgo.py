from __future__ import print_function

import urllib
import urllib2
import urlparse
import json
#
#   we'll use the DuckDuckGo 'Instant Answer' API
#
url='http://api.duckduckgo.com/'
#
#   what to search for?
#
search=raw_input('Enter search string:')
if len(search)==0:
    exit()
#
#   construct the query string by encoding
#   the name:value pairs
#
q=dict(q=search,format='json')
qstring=urllib.urlencode(q)
url='?'.join((url,qstring))
dosave=raw_input('Save downloaded page to disk? [y/n]')
save=dosave in ['y','Y']
print('Requesting',url,'and save?',save)
#
#   execute the query
#
try:
    response = urllib2.urlopen(url)
except Exception,e:
    print(e.__class__.__name__,e)
    exit(0)
#
#   we have a response so save it?
#
if save:
    fname='save.html'
    print('saving to',fname,'...')
    fp=open(fname,'w')
    fp.write(response.read())
    fp.close()
#
#   otherwise display at the terminal
#
else:
    jtext=response.read()
    jcode=json.loads(jtext)
    print(json.dumps(jcode,indent=2,separators=(',', ': ')))