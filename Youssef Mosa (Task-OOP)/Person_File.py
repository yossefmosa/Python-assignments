
class person :
    def __init__(self,name,money,mood,healthRate) :
        self.name=name
        self.money=money
        self.healthRate=self.set_health_rate(healthRate)
        self.mood=mood

    def set_health_rate(self, healthRate):
        if 0 <= healthRate <= 100:
            return healthRate
        else:
            raise ValueError("Health rate must be between 0 and 100.")
        
    def sleep(self,hours) :
        hours=int(hours)
        if hours==7 :
            self.mood="happy"
        elif hours<7 :
            self.mood="tired"
        else :
            self.mood="lazy"
        print(f"{self.name}'s mood is: {self.mood}")

    def eat(self,meals) :
        meals=int(meals)
        if meals==3 :
            self.healthRate=100
        elif meals==2 :
            self.healthRate=75
        else :
            self.healthRate=50
        print(f"{self.name}'s health rate is {self.healthRate} %")

    def buy(self,items) :
        items=int(items)
        self.money-=items*10
        print(f"{self.name}'s money is {self.healthRate}")
