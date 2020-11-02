class Vehicle:
    doors = 4
    tires = 4

    def __init__(self,brand, model, licence_plate):
        self.brand = brand
        self.model = model
        self.licence_plate = licence_plate


    def drive(self):
        print(f'Vehicle {self.brand} {self.model} {self.licence_plate} is riding')

    def stop(self):
        print(f'Vehicle {self.brand} {self.model} {self.licence_plate} stopped')


class Car(Vehicle):

    def drive(self):
        print(f'Car {self.brand} {self.model} {self.licence_plate} is riding on the road ')

    def stop(self):
        print(f'Car {self.brand} {self.model} {self.licence_plate} is staying on the park ')


class Truck(Vehicle):
    tires = 6
    def drive(self):
        print(f'Truck {self.brand} {self.licence_plate} is carrying a load')

    def stop(self):
        print(f'Truck {self.brand} is staying')


vehicle1 = Car('Toyota', 'Camry', 'AH1111AH')
vehicle2 = Truck('Mercedes', 'Arocs', 'AX2222AX')
vehicle3 = Vehicle('Nissan', 'Juke', 'AA3333AA')
print(vehicle2.tires)
vehicle1.drive()
vehicle2.drive()
vehicle3.drive()
vehicle1.stop()
vehicle2.stop()
vehicle3.stop()