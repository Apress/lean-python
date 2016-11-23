from __future__ import print_function
from people import person

#
#   create a new instance of class person
#   for joe bloggs, age 47
#
joe=person('Joe Bloggs',47)
#
#   use the instance variable to verify
#   Joe's name/age
#
print("Joe's age is",joe.age)
print("Joe's full name is ",joe.name)
#
#   add children Dick and Dora
#
joe.addChild('Dick',7)
joe.addChild('Dora',9)
#
#   use thelistChildren method to list them
#
joe.listChildren()
#
#   get the list variable containing Joe's children
#
joekids=joe.getChildren()
#
#   print Joe's details.
#   NB the vars() function lists the values
#   of the instance attributes
#
print("** Joe's attributes **")
print(vars(joe))
#
#   print the details of his children
#   from the list we obtained earlier
#
print("** Joe's Children **")
for j in joekids:
    print(j.name,'attributes')
    print(vars(j))
