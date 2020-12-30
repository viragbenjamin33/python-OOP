
class SpaceShip:

    def __init__(self, fuel, passengers, shields, speedometer):

        self.fuel = fuel
        self.passengers = passengers
        self.shields = shields
        self.speedometer = speedometer

    def list_passengers(self):
        for passenger in self.passengers:
            print("Passenger: {}".format(passenger))

    def add_passenger(self, new_passenger):
        self.passengers.append(new_passenger)
        print("{} was added to the ship".format(new_passenger))

    def travel(self, distance):
        print("trying to travel: {}".format(distance))
        if self.fuel == 0:
            return print("can't go further, tank is empty")
        else:
            self.fuel -= int(distance/2)
            if self.fuel < 0:
                distance -= int(self.fuel*-2)
                print("can only travel: {}".format(distance))
                self.fuel = 0
            if self.fuel < 30 and self.shields == True:
                print("fuel is low, turning off shields...")
                self.shields = False
            self.speedometer += distance
        print("the SpaceShip is at: {}".format(self.speedometer))
        print("the spaceship has: {} fuel".format(self.fuel))


mySpaceShip = SpaceShip(400, ["John", "Steve", "Sam", "Danielle"], True, 0)

mySpaceShip.list_passengers()
mySpaceShip.add_passenger('Lindsay')
mySpaceShip.list_passengers()
mySpaceShip.travel(750)
mySpaceShip.travel(200)
mySpaceShip.travel(100)
