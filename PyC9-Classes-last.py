## Caibidil 9

# print
print('\n\n###\n\nCaibidil :\n\n')
print('Classes...')

### SEE FILE dog.py to see where the Dog Class is stored



######### IMPORTING CLASSES
# Have all Classes stored in another file and when some Class is needed for code just import it.

#IF THE Dog CLASS WAS ON ANOTHER FILE WOULD JUST NEED TO PUT THE FOLLOWING ON THE NEW FILE PROGRAM

from dog import Dog    
# the Dog is the Class in the dog.py file
# dog is a file called dog.py

# an object is needed to be made or instantiated
my_dog = Dog('Tory', 8)  # this is the instance and is the object that has attributes name and age

# needed the values name (Tory) and age(8)
# values can be anything... can have any name or any age

# sit... my_dog.sit()   ... need print to show output to screen only
print(my_dog.sit())



# now roll over... my_dog.roll_over()
print(my_dog.roll_over())



print('\n\nScroll to top to view all outputs!')
