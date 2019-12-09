class car:
    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed= max_speed

    def compareCar(self, car2):
        if self.max_speed > car2.max_speed:
            return self.color + " " +self.model + " is better than "+ car2.color+ " " + car2.model
        else:
            return car2.color + " " + car2.model + " is better than " + self.color + " " + self.model
            
car1 = car("BMW", "Blue", 300)
car2 = car("Mercedes", "Red", 250)
car3 = car("Lamborghini", "Black", 500)

print(car1.compareCar(car2))
print(car1.compareCar(car3))
print(car2.compareCar(car3))