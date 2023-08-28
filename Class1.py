class SedanCar:
    def __init__(self, hp, color, fuel, gb):
        self.horsepower = hp
        self.color = color
        self.fuel = fuel
        self.gearbox = gb

    def car_horn(self):
        print("Boogh")

    def car_break(self):
        print("Tormmmmoz")


# Shey missazim
samand = SedanCar(113, "white", "petrol", "manual")
dena = SedanCar(113, "black", "petrol", "automatic")
