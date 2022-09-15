class Man:

    def __init__(self):
        self.mheight = None
        self.mcolor = None
        self.meye = None
        self.mhair = None

    def create_man(self, height, color, eye, hair):
        self.mheight = height
        self.mcolor = color
        self.meye = eye
        self.mhair = hair

    def print_man(self):
        print(f"The man is {self.mheight}, {self.mcolor}, {self.meye}, {self.mhair}")



m = Man()
m.print_man()
m.create_man("6 feet", "Brown", "Blue", "Black")
m.print_man()
