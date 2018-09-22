class Parent():
    """description of class"""
    def __init__(self,LastName,EyeColor):
        #print "Parent Consetractor Called"
        self.LastName = LastName
        self.EyeColor = EyeColor

class Child(Parent):
    """description of class"""
    def __init__(self,LastName,EyeColor,number_of_toys):
        print "Child Constractor Called "
        Parent.__init__(self,LastName,EyeColor)
        self.number_of_toys = number_of_toys
mina_remon = Child("shaker","blue", 10)
print mina_remon.LastName
print mina_remon.number_of_toys