while True:
    try:
        age = int(input("enter your age : "))
        break
    except:
        print("invalid input")

if age <18:
    print("you can\'t play this game")
else:
    print("you can play this game")

#zero division error
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # print("You cannot divide by zero")
        print(err)
    except TypeError:
        print("You have entered string instead of integer")
    
print(divide(10,"2"))

