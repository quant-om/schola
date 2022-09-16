# Four pillars of Object Oriented Programming
# 1. Abstraction
# 2. Inheritance
# 3. Encapsulation
# 4. Polymorphism

# Classes in Python
class Animal:
    def __init__(self):
        animal_type = None
        animal_color = None


class Car:
    def __init__(self):
        car_type = "SUV"
        car_model = "Maruti"
        car_color = 'Blue'
        car_manu = "Suzuki"
        car_year = 2021
        car_types = []

    def print_car(self):
        print('The car model is maruti brezza')

    def brake_car(self):
        # This function will brake the car
        brake = True
        # Put brakes and exit from this function/method.
        print("Brakes applied, hence car stopped.")

myCar = Car()

myCar.print_car()
myCar.brake_car()

