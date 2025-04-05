
class car :
    def __init__(self,name, fuelRate, velocity) :
        self.name=name
        self.fuelRate=self.set_fuelRate(fuelRate)
        self.velocity=self.set_velocity(velocity)

    def set_velocity (self, velocity):
        if 0 <= velocity <= 200:
            return velocity
        else:
            raise ValueError("velocity must be between 0 and 200.")
        
    def set_fuelRate (self, fuelRate):
        if 0 <= fuelRate <= 100:
            return fuelRate
        else:
            raise ValueError("fuelRate must be between 0 and 100.") 
        
        
    def run (self,velocity,distance) :
        self.distance=distance
        self.velocity=velocity
        initial_fuel=self.fuelRate
        for distance_in_km in range (10,self.distance+1,10) :
            fuel_consumption = initial_fuel*0.1
            self.fuelRate -=fuel_consumption
            if self.fuelRate <= 0 :
                self.remain_distance = self.distance-distance_in_km
                break

        else :
            self.remain_distance =0
        self.stop()
    
    def stop (self) :
        self.velocity=0
        if self.remain_distance == 0 :
            print("You arrive the destintation")
        else :
            print(f"The remain distance is {self.remain_distance}m.")  

