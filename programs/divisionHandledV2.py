from __future__ import print_function
print('Input two numbers. The first will be divided by the second')

afirst = raw_input('first number:')
try:
  first=float(afirst)
  asecond = raw_input('second number:')
  try:
    second = float(asecond)
    try:
      quotient = first / second
      print('Quotient first/second = ',quotient)
    except ZeroDivisionError, e:
      print(e,': Second number must be non-zero')
  except ValueError, e:
    print(e,'Second number')
except ValueError, e:
    print(e,'First number')