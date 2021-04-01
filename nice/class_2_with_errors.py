class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model})>'

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f'<Garage {self.cars}>'

    def __str__(self):
        return f'Garage with {len(self)} cars.'

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
            # raise NotImplementedError("We can't add cars to the garage yet.")
        self.cars.append(car)

# __getitem__ enables1` use of the 'for' loop
# __repr__ used for debugging

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
#ford.add_car('Fiesta')

car = Car('Ford', 'Fiesta')
ford.add_car(car)

print(len(ford))

for car in ford:
    print(car)

print(len(ford))
print(ford[0])
print(ford)
