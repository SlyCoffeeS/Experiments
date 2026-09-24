class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.current_floor = bottom

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            print ("Invalid floor")
            return

        while self.current_floor < floor:
            self.floor_up()

        while self.current_floor > floor:
            self.floor_down()
    
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(self.current_floor)

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print(self.current_floor)


class Building:
    def __init__(self, bottom_floor, top_floor, elevator):
        self.bottom_floor = bottom_floor                # Why does moodle want this, when everything works with out it?
        self.top_floor = top_floor                      # Why does moodle want this, when everything works with out it?
        self.elevators = []

        for i in range(elevator):
            self.elevators.append(Elevator(bottom_floor, top_floor))

        
    def run_elevator(self, elevator_number, destination_floor):
        self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.elevators[0].bottom_floor)
            

# building = Building(1, 10, 3)
# building.run_elevator(0, 5)
# building.run_elevator(1, 8)
# building.run_elevator(2, 3)
# building.fire_alarm()