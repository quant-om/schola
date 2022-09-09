# create a function which adds two numbers
def fun_add(num1, num2):
    val = num1 + num2
    return val
    

b1 = 34
b2 = 58
val = fun_add(b1, b2)
print(f"Addition of {b1} and {b2} is {val}")


class Maths:
    def __init__(self):
        self.num1 = None
        self.num2 = None


    def fun_add(self, num1, num2):
        val = num1 + num2
        return val
    


m = Maths() # class creation / object creation / instantiation

val = m.fun_add(b1, b2)
print(f"Addition of {b1} and {b2} is {val}")

   