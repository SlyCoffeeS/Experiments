class Car:
    def __init__(self, reg_number, max_speed):
        self.registration_number = reg_number
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, change):
        if self.current_speed + change >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change <= 0:
            self.current_speed = 0
        else:
            self.current_speed += change


car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f"Current speed: {car1.current_speed} km/h")
car1.accelerate(-200)
print(f"Current speed: {car1.current_speed} km/h")



## print(f"License plate: {car1.registration_number}")
## print(f"Maximum speed: {car1.maximum_speed} km/h")
## print(f"Current speed: {car1.current_speed} km/h")
## print(f"Travelled distance: {car1.distance} km")