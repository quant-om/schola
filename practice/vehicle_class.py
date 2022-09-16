

"""
class <ClassName>:
    def __init__(self):                 # Double underscore : Dunder method


"""




class Vehicle:
    def __init__(self):
        print("This is init method.")
        self.vtype = None
        self.vmodel = None
        self.vyear = 1980
        self.vcolor = None
        
        color = "black"
        self.color = "red"

        print(f"The color of -varaible color- is {color}")
        print(f"The color of -class variable self.color- is {self.color}")

    def create_vehicle(self, typ, modl, yr, col):
        # In this method we will set the vehicle
        self.vtype = typ
        self.vmodel = modl
        self.vyear = yr
        self.vcolor = col

        print(f"In method : create_vehicle : color is {self.color}")
        #print(f"In method : create_vehicle : color is {color}")  # this is an error, since color is only defined in init method.

    def print_vehicle(self):
        print()
        print(f"The Vehicle is: {self.vtype} {self.vmodel} {self.vyear} {self.vcolor}")
        print()


vh = Vehicle()   # Creating a new Vehicle object : instatiating of Vehicle class : new instance
vh.print_vehicle()

vh.create_vehicle('car', 'Brezza', 2010, 'red')
vh.print_vehicle()

vh.create_vehicle('Bus', 'TATA', 2011, 'Green')
vh.print_vehicle()

# Any class variable or methods can be called by an object of the class 
# <class obj>.<class-method>
# <class obj>.<class-variable>
vh1 = Vehicle()
vh1.print_vehicle()
print(f"The color of vh1 is {vh1.color}")
print(f"The model of vh1 is {vh1.vmodel}")


class Mlist:
    def __init__(self):
        self.top = None
        self.values = None

    def append(self, val):
        self.top += 1
        self.values = val


mylist = list()
mylist.append(6)


mylist1 = Mlist()
mylist1.append(6)