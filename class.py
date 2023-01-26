# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person("john",36)
# print(p1.name)
# print(p1.age)

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name}({self.age})"
# p1=person("john",36)
# print(p1)


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print("hello my name is "+self.name)
# p1=person("john",36)
# p1.myfunc()


# class person:
#     def __init__(mysillyobject,name,age):
#         mysillyobject.name=name
#         mysillyobject.age=age
#     def myfunc(abc):
#         print("hello my name is ",abc.name)
# p1=person("john",36)
# p1.myfunc()


# import array
# for name in array.__dict__:
#     print(name)

# class student:
#     student_name="tarance morales"
#     marks=93
# print(f"student name: {getattr(student,'student_name')}")
# print(f"marks:{getattr(student,'marks')}")
# setattr(student,'student_name','angel brooks')
# setattr(student,'marks',95)
# print(f"student name:{getattr(student,'student_name')}")
# print(f"marks:{getattr(student,'marks')}")

# class pet:
#     def __init__(self):
#         self.__name="no name"
#         self.__animaltype="no type"
#         self.__age=0
#
#     def setname(self,name):
#         self.__name=name
#     def setanimaltype(self,animaltype):
#         self.__animaltype=animaltype
#     def setage(self,age):
#         self.__age=age
#     def getname(self):
#         return self.__name
#     def getanimaltype(self):
#         return self.__animaltype
#     def getage(self):
#         return self.__age
#     def __str__(self):
#         return self.__name + " is a " + str(self. __age) + " year old " + self.__animaltype +"."
#
# def main():
#     print("This program tests the pet class.\n")
#     mypet=pet()
#     mypet.setname(input("pet name:"))
#     mypet.setanimaltype(input("pet type: "))
#     mypet.setage(input("pet age:"))
#
#     print()
#     print("petname:",mypet.getname())
#     print("pettype:",mypet.getanimaltype())
#     print("petage:",mypet.getage())
#     print()
#     print(mypet)
#
# main()


# class student:
#     def __init__(self):
#         self.__name="no name"
#         self.__Class="no class"
#         self.__age=0
#     def setname (self,name):
#         self.__name=name
#     def setclass(self,Class):
#         self.__Class=Class
#     def setage(self,age):
#         self.__age=age
#     def getname(self):
#         return self.__age
#     def getClass(self):
#         return self.__Class
#     def getage(self):
#         return self.__age
#     def __str__(self):
#         return self.__name + " of  age "+str(self.__age)+" study in  "+ self.__Class + " class"
#
# def main():
#     print("this program checks student profile")
#     mystudent=student()
#     mystudent.setname(input("enter student name"))
#     mystudent.setclass(input("enter student class"))
#     mystudent.setage(input("enter the age"))
#     print()
#     print("student name :",mystudent.getname())
#     print("student class :",mystudent.getClass())
#     print("student age :",mystudent.getage())
#     print(mystudent)
# main()

# class Hospital:
#     def __init__(self):
#         self.__name = "no name"
#         self.__age = 0
#         self.__disease = "no disease"
#         self.__room = 0
#         self.__date = 0
#
#     def setname(self, name):
#         self.__name = name
#
#     def setage(self, age):
#         self.__age = age
#
#     def setdisease(self, disease):
#         self.__disease = disease
#
#     def setroom(self, room):
#         self.__room = room
#
#     def setdate(self, date):
#         self.__date = date
#
#     def getname(self):
#         return self.__name
#
#     def getage(self):
#         return self.__age
#
#     def getdisease(self):
#         return self.__disease
#
#     def getroom(self):
#         return self.__room
#
#     def getdate(self):
#         return self.__date
#
#     def __str__(self):
#         return self.__name + " of age " + str(self.__age) + " going through " + self.__disease + " is admitted in room" + str(self.__room) + " from " + str(self.__date)
#
#
# def main():
#     print("This program print the patient profile\n")
#     mypatient = Hospital()
#     mypatient.setname(input("enter patient name :"))
#     mypatient.setage(input("enter patient age :"))
#     mypatient.setdisease(input("enter patient disease :"))
#     mypatient.setroom(input("enter room no :"))
#     mypatient.setdate(input("enter admission date :"))
#     print()
#     print("Patient name : ", mypatient.getname())
#     print("Patient age :", mypatient.getage())
#     print("Patient disease :", mypatient.getdisease())
#     print("Patient room :", mypatient.getroom())
#     print("Patient admission date :", mypatient.getdate())
#     print(mypatient)
#
#
# main()

# class item:
#    pay_rate=0.8#the pay rate after 20 percent discount
#    def __init__(self,name:str,price:float,quantity=0):
#       assert price>=0,f"price{price} is not greater than zero"
#       assert price>=0,f"price{quantity} is not greater than zero"
#       self.name=name
#       self.price=price
#       self.quantity=quantity
#    def calculate_total_price(self):
#       return self.price*self.quantity
#    def apply_discount(self):
#       self.price=self.price*self.pay_rate
# item1=item("phone",500,5)
#
# item2=item("laptop",1000,3)
# item2.pay_rate=0.7
# item2.apply_discount()
# print(item2.price)
#
# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)
# print(item.__dict__)#All the attributes for class level
# print(item1.__dict__)#All the attributes for instance level
# print(item2.__dict__)#All the attributes for instance level
# item1.apply_discount()
# print(item1.price)
# item2.apply_discount()
# print(item2.price)

import csv
class item:
   pay_rate=0.8
   all=[]
   def __init__(self,name,price,quantity):
      #run validation to recieve arguments
      assert price >= 0, f"price{price} is not greater than zero"
      assert price>=0,f"price{quantity} is not greater than zero"
      #assign to self object
      self.name=name
      self.price=price
      self.quantity=quantity
      #actions to execute
      item.all.append(self)
   def calculate_total_price(self):
      return self.price*self.quantity
   def apply_discount(self):
      self.price=self.price*self.pay_rate

   @classmethod
   def instantiate_from_csv(cls):
      with open('items.csv','r') as f:
         reader=csv.DictReader(f)
         items=list(reader)
      for item in items:
         item(
            name=item.get('name'),
            price=float(item.get('price')),
            quantity=int(item.get('quantity')),

         )
   @staticmethod
   def is_integer(num):
      #we will count out the floats that are point zero
      #for i.e: 5.0,10.0
      if isinstance(num,float):
         #count out the floats that are point zero
         return num.is_integer()
      elif isinstance(num,int):
         #count out the floats that are zero
         return True
      else:
         return False

   def __repr__(self):
      return f"item('{self.name}','{self.quantity}','{self.price})"

item1=item("iphone",100,1)
item2=item("laptop",1000,3)
item3=item("cable",10,5)
item4=item("mouse",50,5)
item5=item("keyboard",75,5)
print(item.all)
print(item.is_integer(7.5))

#when to use class method and when to use static method ?


#     type = input("please enter the type of the car: ")
#     name = input('Please enter the name of the car: ')
#     make = input("please enter the make of the car : ")
#     model = input('Please enter the model of the car: ')
#     variant = input('Please enter the variant of the car: ')
#     mileage = input('Please enter the mileage of the car: ')
#     engine_type = input('Please enter the engine_type of the car: ')
#     colour = input('Please enter the colour of  the car: ')
#     rating = input("please enter the rating of the car")
#     registration = input("please enter the registration")
#     registration_city = input("please enter the registration city")
#     chasis_no = input("please enter the chasis_no")
#     price = input("please enter the price")
#     car = elite_motors_buyer(type, name, make, model, variant, mileage, engine_type, colour, rating, registration,
#                              registration_city, chasis_no, price)
#     print("Type: ", car.type())
#     print("Name: ", car.name())
#     print('Make: ', car.make())
#     print('Model: ', car.model())
#     print('variant: ', car.variant())
#     print('Mileage: ', car.mileage())
#     print('engine_type : ', car.engine_type())
#     print('colour : ', car.colour())
#     print("rating from pakwheels: ", car.rating())
#     print("registration : ", car.registration())
#     print("registration_city: ", car.registered_city)
#     print("chasis no: ", car.chasis_no())
#     print("price: ", car.price())
#     print()
