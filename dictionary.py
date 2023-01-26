# from prettytable import PrettyTable
#
# mytable=PrettyTable(["name","make","model","variant","cc","mileage","colour","engine_type","rating","registration_city"
#                                 ,"price"])
# all = []
# make_car = input("Enter the make of the car: ")
# with open('inventory.csv', 'r') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         if make_car==row[2]:
#             all.append(row)
#             print(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
#                   row[13])
# mytable.add_row(make_car.row[1])
# mytable.add_row(make_car.row[2])
# mytable.add_row(make_car.row[3])
# mytable.add_row(make_car.row[4])
# mytable.add_row(make_car.row[5])
# mytable.add_row(make_car.row[6])
# mytable.add_row(make_car.row[7])
# mytable.add_row(make_car.row[8])
# mytable.add_row(make_car.row[9])
# mytable.add_row(make_car.row[10])
# mytable.add_row(make_car.row[11])
# mytable.add_row(make_car.row[13])
# print(mytable)


# list = []
# name = ['name', 'make', 'model', 'variant', 'cc', 'mileage', 'colour', 'engine_type', 'rating', 'registration_city',
#         'price']
# name_car = input("Enter the name of the car: ")
# with open('inventory.csv', 'r') as file:
#     csvreader = csv.reader(file)
#     for list in csvreader:
#         if list[1] == name_car:
#            # row.append(list)
#            print([list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11],
#                    list[13]])
#
# # Create a pandas DataFrame from the list 'all' df = pd.DataFrame(all, columns=['name', 'make', 'model', 'variant',
# 'cc', 'mileage', 'colour', 'engine_type', 'rating', 'registration_city', 'price'])
#
# # Print the DataFrame
# print(df.name)
import csv
from tabulate import tabulate

all_: list = []
headers = ["VEHICLE", "DETAILS"]
name_car = input("Enter the name of the car: ")
with open('inventory.csv', 'r') as file:
    reader = csv.reader(file)
    csv.reader = reader
    for row in csv.reader:
        if row[1] == name_car:
            all_.append(row)
            x = [["name",name_car],["make",row[2]],["model",row[3]],["variant",row[4]],
                 ["mileage",row[5]],["colour",row[6]],["engine_type",row[7]],["cc",row[8]],["rating",row[9]],
                 ["registration_city",row[11]],["price",row[13]]]
            print(tabulate(x,headers=headers))
