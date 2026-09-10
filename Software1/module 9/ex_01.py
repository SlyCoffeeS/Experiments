class Car:
    def __init__(self, reg_number, max_speed):
        self.license_plate = reg_number
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.distance = 0

car1 = Car("ABC-123", 142)

print(f"License plate: {car1.license_plate}")
print(f"Maximum speed: {car1.maximum_speed} km/h")
print(f"Current speed: {car1.current_speed} km/h")
print(f"Travelled distance: {car1.distance} km")