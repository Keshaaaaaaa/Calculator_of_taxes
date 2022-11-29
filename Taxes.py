class Cars():
    def __init__(self, car_name, car_vol, car_year):
        self.car_name = car_name
        self.car_vol = car_vol
        self.car_year = car_year

    def chek_taxes(self):
        print("Налог машины:",self.car_name , self.car_year, "С обьемом", self.car_vol,"будет", (self.car_year * self.car_vol)//4400, "сом")


Mechanic = Cars("Estima", 2400, 2007)

print(Mechanic.chek_taxes())