from Person_File import person
class Employee(person) :
    def __init__(self, name,money,mood,healthRate, id , car, email, salary, distanceToWork):
        person.__init__(self, name,money,mood,healthRate)      
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        
    def __str__(self):
        return f"(Id: {self.id}, Name: {self.name}, Email: {self.email}, Salary: {self.salary})"

    def work(self,hours) :
        hours=int(hours)
        if hours==8 :
            self.mood="happy"
        elif hours>8 :
            self.mood="tired"
        else :
            self.mood="lazy"
        print(f"{self.name}'s mood is: {self.mood}")  

    def drive(self,velocity,distance):
        if self.car :
            print(f"{self.name} with id-{self.id} is driving {distance} km at a velocity {velocity} km/h")
            self.car.run(velocity,distance)
        else :
            print(f"{self.name} with id-{self.id} dosen't have a car")
    
    def refuel(self) :
        self.car.fuelRate +=100


