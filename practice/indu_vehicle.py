class Vehicle:
    def __init__(self):
        print("this is init method")
        self.vtype = None
        self.vmodel = None
        self.vyear = None
        self.vcolor = None

    def create_vehicle(self, typ, modl, year, col):
        self.vtype = typ
        self.vmodel = modl
        self.vyear = year
        self.vcolor = col

    def print_vehicle(self):
        print("The vehicle is:")
        print(f"Type is {self.vtype}")
        print(f"Model is {self.vmodel}")
        print(f"Year is {self.vyear}")
        print(f"Colr is {self.vcolor}")


vh = Vehicle()
vh.print_vehicle()


vh.create_vehicle("car", "Brezza", "2000", "red")
vh.print_vehicle()
