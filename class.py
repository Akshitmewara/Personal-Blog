class Person():
    def __init__(self,name,gmail):
        self.name = name
        self.gmail = gmail
    
    def getinfo(self):
        print("my name: " ,self.name)
        print("gmail: " , self.gmail)
        
class Employee(Person):
    no_of_employee = 50
    
    def __init__(self,Empname,EmpId,pname,gmail):
        self.EmpId = EmpId
        self.Empname = Empname
    
        super().__init__(pname,gmail)
    
    def displayEmp(self,cls):
        cls.no_of_employee = 60
        print(f"my empname: {self.Empname}")
        print("my empId: " , self.EmpId)
        print("total number of employee: " , cls.no_of_employee)
        
p1 = Employee("john",12,"alex","alex@gmail.com")
p1.displayEmp(Employee)
p1.getinfo()

class Salary():
    def __init__(self,name,id,salary) -> None:
        self.name = name
        self.id = id 
        self.salary = salary
        
    def getSalary(self):
        bonus = 5000
        self.salary = bonus + self.salary
        print(self.name,self.id,self.salary)
        
e1 = Salary("akki",1,50000)
e1.getSalary()

