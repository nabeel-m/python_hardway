class Employee:
    empcount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def displaycount(self):
        print("Total employee:",Employee.empcount)
 
    def displayEmployee(self):
        print(self.name,"\t_____|\t",self.salary)

def main():
    print("Name\t_____|\tSalary")
    print("-------------------------")
    
    emp1 = Employee("Arjun", 30000)
    emp1.displayEmployee()
    
    emp2 = Employee("Raj",45000)
    emp2.displayEmployee()  

    emp3 = Employee("Rajesh", 50000)       
    emp3.displayEmployee()
    
    print("\n")
    
    count=Employee.displaycount(Employee.empcount)

if __name__ == "__main__":
    main()