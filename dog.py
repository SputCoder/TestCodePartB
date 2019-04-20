## this file contains the Class Dog... this file is needed for PyC9-Classes-last.py file

class Dog():      # the colon : is needed is like start of brackets { }.. in C#
    # a container to store data (=attributes) and actions (=methods)
    # attributes and methods

    def __init__(self, name, age):
        # initialises name and age attributes
        self.name = name
        self.age = age

    def sit(self): 
        # action or method
        return self.name + " is now sitting"

    def roll_over(self):
        # another method
        # let's say the dog can roll
        return self.name + " rolled over"

# the class ends here just what is tabbed beneath class Dog(): as above