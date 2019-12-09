class example:
    
    def __init__(self, my_str):
        self.my_str = my_str
    
    def get_String(self):
        return self.my_str

    def print_String(self):
        print(self.my_str.upper())

x = example("Lalala")      
print(x.get_String())
x.print_String()