# OOP - class inheritance

'''
Base model car with seats, engine, wheels
Sports model car with poweful engine, high end seats
have common features then adds or modify some features
'''

class Car:
    def __init__(self):
        self.wheels = 4
        self.seats = 5
        
    def drive(self):
        print("Driving a car...")

# lets inherit the Car class into our SportsCar class
class SportsCar(Car):
    def __init__(self):
        super().__init__() # init the parent class so we don't loose the attribues
        self.engine_power = '400 HP' # adds a new attribute for the sports class class
        self.sets = 2 # redefins an inherited attribute from the car class for the sports car class
    
    # re-init our drive function for the Sports Car Class    
    def drive(self):
        print("Driving a Sports Car")

# if we instantiate the car class and call the drive method what happens?        
myCar = Car()
myCar.drive()
mySportsCar = SportsCar()
mySportsCar.drive()

'''
SportsCar has inherited the base attribues and functions or the car class
Seats was changed from 5 to 2 for the sports car
add a new engine power attribute
the drive function from the car class was overriden in the sports car class to say driving a sports car
