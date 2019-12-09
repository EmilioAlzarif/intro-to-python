class Police_car:
    tax_value = 0.2
    def __init__(self, owner, price, pass_code):
        self.owner = owner
        self.price = price
        self.__pass_code = pass_code
    
    def tax(self):
        return Police_car.tax_value*self.price
    
    def greeting(self):
        if self.__pass_code == "Admin":
            print("Welcome to your car", self.owner)
        else:
            print(self.owner, "Your Access is Denied")
    
    def set_code(self, new_code):
        self.__pass_code = new_code
    
    def get_code(self):
        return self.__pass_code

x = Police_car("Police", 100, "Admin")
x2 = Police_car("Emil", 50, "Emilio")

x.greeting()
print("Your Tax is :", x.tax())

x2.greeting()
print("Your Tax is :", x2.tax())

x2.set_code("Admin")
print(x2.owner,"you changed your pass_code to", x2.get_code())

x2.greeting()
print("Your Tax is :", x2.tax())