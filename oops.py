#Object oriented programming

class Person: #to create a class, first letter of the class name should be capital as per convention
    count_instance = 0
    def __init__(self, first_name, last_name, age, gender):
        Person.count_instance +=1
        #instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
#we want to create class method as a constructor
    @classmethod
    def from_string(cls, string):
        first,last,age,gender = string.split(',')
        return cls(first,last,age,gender)
# we want to define class method - so we use decorator @classmethod and pass the function
    @classmethod
    def count_ins(cls):
        return f"You have made {cls.count_instance} instances for {cls.__name__} class"
# we will use static method decorator
    @staticmethod
    def hello():
        print('hello, static method called')    
# we want to define the full name of the class person..we will define a new method
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
# we want to define a function for the age
    def is_above_18(self):
        if self.age >18:
            print(f"{self.first_name} is above 18")
        else:
            print(f"{self.first_name} is below 18")

#self will act as a object that we will define while calling our function

p1 = Person("Swati", "Gupta", 27, "Female")
p2 = Person("Kushal", "Bansal", 27, "Male")
p3 = Person("palak", "Gupta", 18, "Female")
p4 = Person.from_string("megha,gupta,25,female")

print(p1.first_name)
print(p2.last_name)
print(p3.age)
print(p1.full_name())
print(p2.full_name())
print(p3.full_name())
print((p3.is_above_18()))
print(Person.count_ins())
print(type(p4.age))
Person.hello()

#static method - it is linked with the class not with the object
