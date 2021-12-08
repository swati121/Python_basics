#multilevel Inheritance - when we use class1 -> class 2 -> class 3
# here smartphone is derived from phone class and flagship class is derived from smartphone.

class Phone: #base class/parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def specs(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    def make_call(self,phone_number):
        print(f"calling {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

#str method - Nicely formatted string
#repr method - representation of the code

#polymorphism - when an operator is used in many different forms in a code.
#2+3 = 5 & 'abc' + "def" = abcdef
#here, + operator is playing different roles at the same time. Hence it is polymorphism.

class Smartphone(Phone): #derived class/child class
    def __init__(self, brand, model_name, price, ram, camera, memory):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.camera = camera
        self.memory = memory

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

class Flagship(Smartphone): #derived class/child class
    def __init__(self, brand, model_name, price, ram, camera, memory, front_camera, origin):
        super().__init__(brand, model_name, price, ram, camera, memory)
        self.front_camera = front_camera
        self.origin = origin

#method Resolution order - it is the help method for a class to know about the chronology and associated class/method with
#the particular class.

#Method Overriding - to define same method in a particular class with different values

#isintance & issubclass

#Mutiple Inheritance
class Iphone(Smartphone):
    pass

p1 = Phone("samsung", "s9", 60000)
sp1 = Smartphone("honor", "8X", 15000, "4GB", "16MP", "64GB")
flag = Flagship("moto", "g5", 10000, "4GB", "16MP", "128GB", "8MP", "Australia")
i1 = Iphone("i", "6s", 70000, "16GB", "64MP", "128gb")


# print(p1.full_name())
# print(sp1.full_name())    
# print(flag.full_name())
# print(help(Flagship))
print(i1.full_name())

