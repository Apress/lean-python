from __future__ import print_function
import sys

nargs=len(sys.argv)
print('%d argument(s)' % (nargs))
n=0
for a in sys.argv:
    print('  arg %d is %s' % (n,a))
    n+=1
