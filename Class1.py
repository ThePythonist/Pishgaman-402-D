import time


class SedanCar:
    def __init__(self, hp, color, fuel, gb):
        self.horsepower = hp
        self.color = color
        self.fuel = fuel
        self.gearbox = gb
        self.rpm = 0

    def car_horn(self):
        print("Boogh")

    def car_break(self):
        print("Tormmmmoz")

    def accelerate(self, value):
        for i in range(value):
            time.sleep(2)
            self.rpm += 1000
            print(self.rpm)


# Shey missazim
samand = SedanCar(113, "white", "petrol", "manual")
dena = SedanCar(113, "black", "petrol", "automatic")

dena.accelerate(value=3)
