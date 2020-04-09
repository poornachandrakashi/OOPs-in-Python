class Employess():
    #Definiing the initializers
    def __init__(self,ID=None,salary=None,department=None):
        self.ID=ID
        self.salary=salary
        self.department=department

    def tax(self):
        return(self.salary*0.2)

    def salaryperday(self):
        return(self.salary/30)


#Initializing the object to the Employess class
poorna=Employess(2525,20000000,"Artificial intelligence")
print("Id=",poorna.ID)
print("Salary=",poorna.salary)
print("Department=",poorna.department)
print("Tax=",poorna.tax())
print("Salary per Day=",poorna.salaryperday())
