#lets start with crud on grocery list
my_list = [
    {'name' : 'bread', 'price': 0.5, 'quantity' : 20},
    {'name' : 'milk', 'price': 1, 'quantity' : 30},
    {'name' : 'butter', 'price': 2, 'quantity' : 10},
    {'name' : 'yogurt', 'price': 3, 'quantity' : 35},
]

#create functionality
items = list() #it will be a global variable where we store all data
def create_items(app_items):
    global items
    items = app_items

def create_item(name, price, quantity):
    global items
    items.append({'name' : name, 'price': price, 'quantity' : quantity})

#read functionality
# def read_item()

