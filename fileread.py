#read file -  to read the contents of the file
#tell method - to check the position of cursor in the txt file.
#seek method - to change the position of the cusrsor in file.
#readline method - to read one line at a time.
#readlines - to convert all matter of file into one list

# f1 = open('file.txt')
# lines = f1.readlines()
# print(lines)
# # print(f'cursor position = {f1.tell()}')
# # print(f1.read())
# # print(f1.readline())
# # print(f1.readline())
# # print("before seek method")
# # print(f'cursor position = {f1.tell()}')
# # print("after seek method")
# # f1.seek(0)
# # print(f'cursor position = {f1.tell()}')
# # print(f1.read())
# f1.close()

# l = [125000, 75000, 46000, 45000]
# total = 0
# for x in range(0, len(l)):
#     total += l[x]/len(l)

    
# print(f"the average salary is {int(total)} dollars.")

from csv import DictReader

with open("employees.csv", "r") as rf:
    salary = DictReader(rf)
    for x in (salary):
        dict_items = print(x)

print(dict_items)