import time

class Person:
    def __init__(self, name, last_name, age, gender, student, password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password
        
        try:
            if type(self.student) != bool:
                raise Exception
        except Exception:
            print("Student type must be boolean attribute, it takes values True/False")
    
    def dec(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print("The Execution of the method Greeting took", end_time-start_time, "time !")
        return wrapper


    @dec
    def Greeting(self, second_person):
        print("Welcome dear", second_person.name)

    def Goodbye(self):
        print("Bye Everyone !")

    def Favourite_num(self, num1):
        try:
            if num1<0:
                raise Exception
        except Exception:
            print("please enter a positive number")
        else:
            print("My favourite number is", num1)
    
    def Read_file(self, filename):
        try:
            file_name = open(filename + ".txt")
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
        else:
            print(file_name.name)

    def set_pass(self, new_password):
        self.__password = new_password
    
    def get_pass(self):
        return self.__password

p1 = Person("Emil", "Alzarif", 26, "Male", "lala", "Admin")
p2 = Person("Kristina", "Sahakyan", 26, "Female", False, "notAdmin")

p1.Greeting(p1)
p1.Greeting(p2)

p1.Favourite_num(2)
p2.Favourite_num("4")

p1.Read_file("halo")

print(p2.get_pass())
p2.set_pass("Admin")
print(p2.get_pass())

p1.Goodbye()

