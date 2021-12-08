class laptop:
    disc_percent = 10 #this will be treated as class variable as it will be same throughout the class
    def __init__(self, brand_name, model, price):
        self.brand_name = brand_name
        self.model = model
        self.price = price
    def discount(self):
        return self.price - (self.disc_percent/100)*self.price

#if we want to end the discount
laptop.disc_percent = 0

p1 = laptop("Lenovo", "s145", 25000)
p2 = laptop("HP", "Pavilion g5", 30000)
p2.disc_percent = 50

print(p1.discount())
print(p2.discount())
#if we want to check the variable inside the object
print(p1.__dict__)
print(p2.__dict__)
#if we want to apply discount in a particular product..then we use self instead of class name
