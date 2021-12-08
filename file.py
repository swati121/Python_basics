# #r mode-read
# #w - write
# #a - 
# pricePerPerson = 21_000
# print(pricePerPerson)
# # here _ will work as a seperator

# x="dog"
# y='cat'
# print("the "+ x + " chases the " +y)
# print(x*3)

# print("hens", 25+30/6)

# print(3+2 > 5-7)

# print(3+2+1-5+4%2-1/4+6)

# print("roosters", 100-25*3%4)
# print(25*3%4)

# a = float("3.2")**2*3.14
# print(a)

# print(1.0+int(float("3.1"))%2)
# # print(round(int(1)*2.0)+str("0"))
# # print(int(1.0)+int(float("1.1")))



# # a_1 = 1.0 + int("3.1")
# # print(a_1)

# c = str(round(int(1) * 2.0)) + "0"
# print(type(c))

# g_1 = set((input("Enter the number group 1: ")).split(" "))
# g_2 = set((input("Enter the number group 2: ")).split(" "))
# print(type(g_1))
# print(type(g_2))

# r = g_1 & g_2
# print(r)

list_type = [
    {"type": "Square", "area": 150.5},
    {"type": "Rectangle", "area": 80},
    {"type": "Rectangle", "area": 660},
    {"type": "Circle", "area": 68.2},
    {"type": "Triangle", "area": 20},
]

# d_1 = print(list_type[0])
# d_2 = print(list_type[1])
# d_3 = print(list_type[2])
# d_4 = print(list_type[3])
# d_5 = print(list_type[4])

# for x in range(len(list_type)):
#     print(list_type[x]["type"], list_type[x]["area"])

class Shape:
    def __init__(self, shape_index, shape_type, shape_area):
        self.index = shape_index
        self.type = shape_type
        self.area = shape_area
    
    def print_shape(self):
        print(f'{self.index} - {self.type} with area size {self.area}')

for x in range(len(list_type)):
    if list_type[x]["type"] == "Square":
        s1 = Shape(x + 1, list_type[x]["type"], list_type[x]["area"])
        s1.print_shape()
    elif list_type[x]["type"] == "Triangle":
        t1 = Shape(x + 1, list_type[x]["type"], list_type[x]["area"])
        t1.print_shape()
    elif list_type[x]["type"] == "Rectangle":
        r1 = Shape(x + 1, list_type[x]["type"], list_type[x]["area"])
        r1.print_shape()
    else:
        list_type[x]["type"] == "Circle"
        c1 = Shape(x + 1, list_type[x]["type"], list_type[x]["area"])
        c1.print_shape()
    

print(s1)
    
