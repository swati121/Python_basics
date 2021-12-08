#exercise 1 - oop
class laptop:
    def __init__(self, brand_name, model, price):
        self.brand_name = brand_name
        self.model = model
        self.price = price
    def discount(self,x):
        return self.price - (x/100)*self.price



p1 = laptop("Lenovo", "s145", 25000)
p2 = laptop("HP", "Pavilion g5", 30000)
print(type(p1))

#exercise 2 - define a function that will apply discount on the price

print(p1.discount(40))
print(p2.discount(35))

#exercise 3 - define class and count the instance/objects created under that class
class Teacher:
    count_instance = 0
    def __init__(self, first_name, last_name):
        Teacher.count_instance +=1
        self.first_name = first_name
        self.last_name = last_name
        
t1 = Teacher("swati", "gupta")
t2 = Teacher("kushal", "bansal")
t3 = Teacher("megha", "gupta")
print(Teacher.count_instance)