from inheritance_car import Car


class Petrol_Car(Car):

    def __init__(self, fuel_tank, *args):
        self.fuel_tank = fuel_tank
        Car.__init__(self, *args)

    def print_details(self):
        Car.print_details(self)
        print('Fuel capacity (gallons): ' + str(self.fuel_tank))


mm = Petrol_Car(30, 'SUV', 'X5', 'silver', 2003, 120300)
mm.print_details()
