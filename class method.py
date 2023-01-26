class employee:
    no_of_leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printdetails(self):
        return f"The name is {self.name}.salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    @classmethod
    def from_str(cls,string):
        # params=string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
harry=employee.from_str("harry-255-instructor")
rohan=employee.from_str("rohan-455-student")
karan=employee.from_str("karan-480-student")

print(karan.salary)
print(rohan.role)
print(harry.role)