# # class Myclass:
# #     def show(self):
# #         print("i am method")
# # x=Myclass()
# # x.show()
#
# class Mobile:
#     def __init__(self,m):
#         self.model=m
#     def show_model(self,p):
#         self.price=p
#         print("Model:",self.model,"price:",self.price)
# realme=Mobile("RealMe x")
# # realme.show_model()
# realme.model="Realme Pro2"
# print(realme.model)
# realme.show_model(1000)
# print(id(realme))
# print()
# redmi=Mobile("redmi 7s")
# redmi.show_model(2000)
# print(id(redmi))
# print()
# geek=Mobile("python")
# geek.show_model(49)
# print(id(geek))
from datetime import datetime
# dt1=datetime(year=2019,month=6,day=30)
# dt2=datetime(year=2018,month=5,day=29,hour=15,minute=34)
# dt3=datetime(2017,4,28)
# dt4=datetime(2016,3,27,14,30)
# print(dt1)
# print(dt2)
# print(dt3)
# print(dt4)
from datetime import datetime
class attendance(employee):
    def __init__(self,employeeno,date,day,timein,timeout,breakin,breakout):
        self.employeeno = employeeno
        self.date=date
        self.day=day
        self.timein=timein
        self.timeout=timeout
        self.breakin=breakin
        self.breakout=breakout

    ct = datetime.now()          #office start
    ct_1=timedelta(minutes=540)   #leave office
    ct_2 = timedelta(minutes=180)   #leave for break
    ct_3=timedelta(minutes=240)   #enter from break
    ct1=(ct+ct_1)
    ct2=(ct+ct_2)
    ct3=(ct+ct_3)
    # employeeno=input("enter the employee no : ")
    # timein = print("entry time : ",ct)
    # timeout = print("exit time :",ct1)
    # breakout = print("leaving for break", ct2)
    # breakin =print("enter from break",ct3)

    @classmethod
    def instantiate_from_csv(cls):
        with open('attendance.csv', 'a', newline="") as csvfile:
            fieldnames = ["employeeno", "timein", "timeout","breakin","breakout"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            while True:
                employeeno=input("enter employeeno")
                timein=input("enter the time of entering the office : ")
                timeout=input("enter the time of leaving the office : ")
                breakin=input("enter the time for entering the office after break : ")
                breakout=input("enter the time of leaving the office for break : ")
                employeeno=input("enter the employee no : ")
                timein = print("entry time : ",ct)
                timeout = print("exit time :",ct1)
                breakout = print("leaving for break", ct2)
                breakin =print("enter from break",ct3)
                with open("attendance.csv") as f:
                    reader = csv.reader(f)
                    header = next(reader)
                if header == "":
                    writer.writeheader()
                writer.writerow(
                { "employeeno": employeeno,"timein":timein, "timeout":timeout,"breakin":breakin,"breakout":breakout })
                break



