class Car:
    def __init__(self):
        car_type = None
        car_model = "Maruti"
        car_year = None
        car_types = []
    def print_car(self):
        print("The car model is Maruti brezza")
    def brake_car(self):
        brake = True
        print("Brakes are applied hence car stopped")

myCar = Car()

myCar.print_car()
myCar.brake_car()