class Vehicle:
    def __init__(self, number_of_wheels, color, engine):
        self.number_of_wheels = number_of_wheels
        self.color = color
        self.engine = engine

    def im_a_vehicle(self):
        print('I am a vehicle')


class Car(Vehicle):
    def __init__(self, number_of_wheels, color, engine, number_of_airbags):
        super().__init__(number_of_wheels, color, engine)
        self.number_of_airbags = number_of_airbags
        print(self.number_of_wheels)

    def __str__(self):
        return f'This is a car. It has number of wheels : f{self.number_of_wheels} +f{self.engine}'


car = Car(4, 'Red', 'blabal', 2)
car.im_a_vehicle()
print(car)
