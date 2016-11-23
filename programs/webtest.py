from __future__ import print_function

import urllib
import urllib2
import urlparse

path=''
url=raw_input('Web url to fetch:')
urlparts=urlparse.urlparse(url)
if urlparts[0]=='':
    url=''.join(('http://',url))
print(str(urlparts))

qstring=raw_input('Enter query string:')

save=raw_input('Save downloaded page to disk [y/n]?')
if len(qstring)>0:
    url='?'.join((url,qstring))
    
print('Requesting',url)

try:
    response = urllib2.urlopen(url)
    if save.lower()=='y':
        geturl=response.geturl()
        urlparts=urlparse.urlparse(geturl)
        for p in urlparts:
            print(p)
        path=urlparts[2]
        if len(path)==0:
            fname='save.html'
        else:
            fname='_'.join(path.split('/'))
            fname='_'.join(path.split('\\'))
            fname='.'.join((fname,'html'))
        print('saving to',fname,'...')
        fp=open(fname,'w')
        fp.write(response.read())
        fp.close()
    else:
        print(response.read())
except Exception,e:
    print(e.__class__.__name__,e)


