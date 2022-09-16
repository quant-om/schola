


class Vehicle:
    def __init__(self):
        print("This is init method.")
        self.vtype = None
        self.vmodel = None
        self.vyear = 1980
        self.vcolor = None

    def create_vehicle(self, typ, modl, yr, col):
        # In this method we will set the vehicle
        self.vtype = typ
        self.vmodel = modl
        self.vyear = yr
        self.vcolor = col

    def print_vehicle(self):
        print()
        print(f"The Vehicle is: {self.vtype} {self.vmodel} {self.vyear} {self.vcolor}")
        print()


vh = Vehicle()
vh.print_vehicle()

vh.create_vehicle('car', 'Brezza', 2010, 'red')
vh.print_vehicle()

vh.create_vehicle('Bus', 'TATA', 2011, 'Green')
vh.print_vehicle()

vh1 = Vehicle()
vh1.print_vehicle()