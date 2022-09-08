class man:

    def __init__(self):
        self.mheight = None
        self.mcolor = None
        self.meye = None
        self.mhair = None

    def creat_man(self, height, color, eye, hair):
        self.mheight = height
        self.mcolor = color
        self.meye = eye
        self.mhair = hair

    def print_man(self):
        print()
        print(f"The man is {self.mheight} {self.mcolor} {self.meye} {self.mhair}")
        print()

m = man()
m.print_man
m.creat_man('6 feet', 'brown', 'blue','black')
m.print_man()

