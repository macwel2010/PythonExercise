class Car:
    def init(self, year_model: str, make: str, speed):
        self.year_model = year_model
        self.make = make
        self.speed = 0

    def accelerate(self, speed):
        self.speed = self.speed + 5

    def brake(self, speed):
        self.speed = self.speed - 5

    def get_speed(self):
        return self.speed


car = Car()
car.year_model = input("Enter the year model of the car : ")
car.make = input("Enter the make of the car : ")
car.speed = input("enter the speed of the car : ")

for i in range(5):
    car.accelerate(car.speed)
    print("this is object car for accelerator : ", car.speed)
for i in range(5):
    car.brake(car.speed)
    print("this is object car for brake : ", car.speed)
