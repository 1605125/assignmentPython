class Car:
    def __init__(self, typ, make, color, year, miles):
        self.typ = typ
        self.make = make
        self.color = color.lower()
        self.year = year
        self.miles = miles

    def print_details(self):
        print('Vehicle Type: {}'.format(self.typ))
        print('Make: {}'.format(self.make))
        print('Color:{} '.format(self.color))
        print('Year: {}'.format(self.year))
        print('Miles driven: {}'.format(self.miles))


class Petrol_car(Car):

    def __init__(self, fuel_tank, typ, make, color, year, miles):
        self.fuel_tank = fuel_tank
        super(Petrol_car, self).__init__(typ, make, color, year, miles)

    def print_details(self):
        super(Petrol_car, self).print_details()
        print('Fuel capacity (gallons): {}'.format(self.fuel_tank))


class Diesel_Car(Car):

    def __init__(self, fuel_tank, *args):
        self.fuel_tank = fuel_tank
        Car.__init__(self, *args)

    def print_details(self):
        Car.print_details(self)
        print('Fuel capacity (gallons): {}'.format(self.fuel_tank))


class Maruti(Petrol_car):

    def __init__(self, model, *args):
        self.model = model
        Petrol_car.__init__(self, *args)

    def print_details(self):
        super(Maruti).print_details()
        print('Model: {}'.format(self.model))


class Hyundai(Diesel_Car):

    def __init__(self, model, fuel_tank, typ, make, color, year, miles):
        self.model = model
        super(Hyundai, self).__init__(fuel_tank, typ, make, color, year, miles)

    def print_details(self):
        super(Hyundai, self).print_details()
        print('Model: {}'.format(self.model))


# mm = Diesel_Car(30, 'SUV', 'X5', 'silver', 2003, 120300)
# mm.print_details()
# print("====================")
# nn = Petrol_car(40, 'bmw', 'i5', 'red', 1988, 140398)
# nn.print_details()

