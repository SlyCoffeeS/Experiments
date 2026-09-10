import random
class Car:
    def __init__(self, reg_number, max_speed):
        self.license_plate = reg_number
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        if self.current_speed + change >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change <= 0:
            self.current_speed = 0
        else:
            self.current_speed += change

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

def race(cars):
    cars.clear()            ## didnt know how to fix my code without this :( kept returning 20, and if changed then moddle complained.
    for i in range(10):
        car = Car(f"ABC-{i+1}", random.randint(100,200))
        cars.append(car)
    return cars

cars = []
cars = race(cars)

while all(car.travelled_distance <= 10000 for car in cars):
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        
for car in cars:
    print(f"The car {car.license_plate} speed is {car.current_speed} and has driven this distance: {car.travelled_distance}")