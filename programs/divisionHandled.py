from __future__ import print_function
print('Input two numbers. The first will be divided by the second')

afirst = raw_input('first number:')
asecond = raw_input('second number:')

try:
    first=float(afirst)
    second = float(asecond)
    quotient = first / second
    print('Quotient first/second = ',quotient)
except Exception, e:
    print(e.__class__.__name__,':',e)
    
