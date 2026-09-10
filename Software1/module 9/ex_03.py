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



car1 = Car("ABC-123", 142)

car1.accelerate(60)
car1.drive(1.5)



## print(f"License plate: {car1.license_plate}")
## print(f"Maximum speed: {car1.maximum_speed} km/h")
## print(f"Current speed: {car1.current_speed} km/h")
## print(f"Travelled distance: {car1.distance} km")