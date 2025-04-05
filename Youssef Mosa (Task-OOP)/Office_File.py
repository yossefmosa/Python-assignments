
class office () :
    employeesNum=0
    def __init__(self,name) :
        self.Current_Employees = []
        self.name=name
    
    def get_all_employees (self) :
        num =0
        for emp in self.Current_Employees :
            num+=1
            print (f"Employee ({num})------{emp}")
        
    def getwithspecificid (self,emp_id) :
        for emp in self.Current_Employees :
            if emp_id == emp.id  :
                return emp
 
    def get_employee (self,emp_id) :
        for emp in self.Current_Employees :
            if emp_id == emp.id  :
                print (f"{emp.name} with id-{emp.id} is an employee in {self.name} office.")
                break
        else:
            print (f"This employee is not in {self.name} office")           
       

    def hire (self,employee) :
        self.Current_Employees.append (employee)
        office.employeesNum+=1
        print(f"{employee.name} with id-{employee.id} has been hired at {self.name} office.")

    def fire (self,emp_id) :
        emp = self.getwithspecificid(emp_id)
        if emp :
            self.Current_Employees.remove (emp)
            office.employeesNum-=1
            print(f"{emp.name} with id-{emp.id} has been fired from {self.name} office.")
    
    @classmethod
    def change_emps_num (cls, num):
        employeesNum += num

    @staticmethod
    def calculate_lateness (target_hour , move_hour, distance, velocity) :
        arrival_hour=move_hour + (distance/velocity)
        if arrival_hour>target_hour :
            print ("the employee is late")
        else :
            print ("the employee is not late")

    def check_lateness (self,emp_id, target_hour , move_hour, distance, velocity) :
        emp = self.getwithspecificid(emp_id)
        if emp :
            arrival_hour=move_hour + (distance/velocity)
            if arrival_hour>target_hour :
                print (f"the employee with {emp_id} is late")
                self.deduct(emp_id, 10)
            else :
                print (f"the employee with {emp_id} is late")
                self.reward(emp_id, 10)
        else :
            print (f"Employee not found in {self.name}")


    def deduct (self, emp_id, deduction) :
        emp = self.getwithspecificid(emp_id)
        if emp :
            emp.salary-=deduction
            print (f"Deduce {deduction} L.E deducted from the salary of {emp.name} with id-{emp.id}")
        else :
            print (f"Employee not found in {self.name}")
        
    def reward (self, emp_id, reward) :
        emp = self.getwithspecificid(emp_id)
        if emp :
            emp.salary-=reward
            print (f"reward {reward} L.E added from the salary of {emp.name} with id-{emp.id}")
        else : 
            print (f"Employee not found in {self.name}")


   


