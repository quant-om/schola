class Tree:
    def __init__(self):
        print("It is a big plant")

        self.pleaf = None
        self.pfruit = None
        self.pbranch = None

    def create_tree(self, leaf, fruit, branch):
        self.pleaf = leaf
        self.pfruit = fruit
        self.pbranch = branch

    def print_tree(self):
        print(f"leaf is {self.pleaf}")
        print(f"Fruit is {self.pfruit}")
        print(f"branch = {self.pbranch}")

tr = Tree()
tr.print_tree()

tr.create_tree("mangoleaf", "mangofruit", "mangobranch")
tr.print_tree()


class Animal:
    def __init__(self):
        print("Attributes of an Animal are:")
        self.acolor = None
        self.alegs = None
        self.askin = None
        self.atail = None

    def create_animal(self, color, legs, skin, tail):
        self.acolor = color
        self.alegs = legs
        self.askin = skin
        self.atail = tail

    def print_animal(self):
        print(f"color of animal is {self.acolor}")
        print(f"legs of animal are {self.alegs}")
        print(f"skin of animal is {self.askin}")
        print(f"tail of animal is {self.atail}")

an = Animal()
an.print_animal()

an.create_animal("yellow", "four", "fur", "long")
an.print_animal()


