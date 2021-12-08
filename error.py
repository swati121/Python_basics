#NotImplemented error
#abstract method
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        raise NotImplementedError("you have to define this method in each subclass")

# we want to define sound method for each class otherwise there should be an error.
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        return "bhow"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "meo"

d1 = Dog("Jimmy", "lebra")
c1 = Cat("kitty", 'black')

print(d1.sound())
print(c1.sound())

#error Part 2 - here we will discuss type error
class Mobile:
    def __init__(self, name):
        self.name = name

class MobilePhone:
    def __init__(self):
        self.mobiles = []
    
    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("Please create instance under Mobile Class")
    
p1 = Mobile("oneplus")
p2 = Mobile("Samsung")
p3 = Mobile("Apple")
p4 = Mobile("Honor")
honor = "Honor 8X"
m1 = MobilePhone()
m1.add_mobile(p1)
m1.add_mobile(p2)
m1.add_mobile(p3)
m1.add_mobile(p4)

phone_new = m1.mobiles
print(phone_new[0].name,phone_new[1].name)