#encapsulation, abstraction, naming convention, name mangling

#under namimg convention we use _ to tell the user that this variable or method is private.
# __name__ = dunder/magic method 

#name mangling  - __name (not a convention) but python will change the name of the variable.
class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
         #if user wants to enter a negative input in price which is practically not possible, then we will use max function
        self._price = max(price,0) #_price will indicate that it is private method.
        # self.specs = f"{self.brand} {self.model_name} and price is {self._price}"
    @property
    def specs(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"
    def make_call(self,phone_number):
        print(f"calling {phone_number}")
    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone1 = Phone("Samsung", "s9", 60000)

phone1._price = 100000
print(phone1._price)
print(phone1.specs) #we have used property decorator in order to call the property of the class
