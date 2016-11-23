from __future__ import print_function
import re         # The RegEx library
#
# our regular expression (to find emails)
# and text to search
#
regex = '\s[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}[\s\.]'
text="""This is some text with x@y.z embedded emails
that we'll use as@example.com
some lines have no email @ddresses
others@have.two valid email@addresses.com
The re module is awonderful@thing."""
print('** Search text ***\n'+text)
print('** Regex ***\n'+regex+'\n***')
#
#   uppercase our text
utext=text.upper()
#
#   perform a search
m = re.search(regex,utext)
if m:
    print('Search found','"'+m.group()+'"')
#
#   find all matches
m = re.findall(regex,utext)
if m:
    for match in m:
        print('Match found',match.strip())
