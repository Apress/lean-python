from mod1 import *

hello()
hello.writtenby='xxx'
print 'written by', hello.writtenby
print mod1.writtenby

greet = greeting()
greet.morning()
greet.evening()