g=9.8

def weight_Calc(m):
    f=m*g
    return f


class car():
     
    # init method or constructor
    def __init__(self, mk, mdl, clr, yr): # define attributes of the class car
        self.model = mdl
        self.color = clr
        self.make = mk
        self.year = yr
         
    def show(self): # define a method associated with car
        print("\nModel is", self.model )
        print("color is", self.color )
        print("Make is", self.make)
        print("Year is", self.year)
         
