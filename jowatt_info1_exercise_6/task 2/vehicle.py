import sys

class Vehicle(object):
    ######## CODE MISSING HERE

    vehicle_id = 0
    vehicles_sold = []

    def __init__(self,year,mileage,purchase_price,serial_number):
        pass
    ######## CODE MISSING HERE

        try:
            self.__year = int(year)
            self.__mileage = int(mileage)
            self.__purchase_price = int(purchase_price)
        except ValueError:
            print('Error! Year, mileage and price have to be integers!')
        self.__serial_number = serial_number
        
    ######## CODE MISSING HERE

    def __str__(self):
        pass
    ######## CODE MISSING HERE

        return str(self.get_id())

    def get_id(self):
        pass
    ######## CODE MISSING HERE

        return self.generate_vehicle_id(self)

    @staticmethod
    def generate_vehicle_id(self):
        pass
    ######## CODE MISSING HERE

        return Vehicle.vehicle_id + 100000

class Car(Vehicle):

    def __init__(self,year,mileage,purchase_price,serial_number,doors):
        pass
    ######## CODE MISSING HERE

        Vehicle.__init__(self, year, mileage, purchase_price, serial_number)

        self.__doors = doors
        self.__wheels = 4

class Lorry(Vehicle):

    def __init__(self,year,mileage,purchase_price,serial_number,wheels,doors=2):
        pass
    ######## CODE MISSING HERE

        Vehicle.__init__(self,year,mileage,purchase_price,serial_number)

        self.__wheels = wheels
        self.__doors = doors
        
class Motorcycle(Vehicle):

    ######## CODE MISSING HERE

    classic_count = 0


    def __init__(self,year,mileage,purchase_price,serial_number,classic=False):
        pass
    ######## CODE MISSING HERE

        Vehicle.__init__(self,year,mileage,purchase_price,serial_number)

        self.__classic = classic

        if classic == True:

            Motorcycle.classic_count += 1

### test cases ###

# initialising vehicle instances

Veh1 = Vehicle(2008,65000,7500,"34567851g4")
Veh2 = Car(2007,125000,5500,"e44653ftu1",4)
Veh3 = Car(2012,45000,8900,"gf5622iguz",doors=2)
Veh4 = Lorry(2005,180000,16000,"hbh997123f",6)
Veh5 = Lorry(2013,30000,35000,"hjbf17jbkh",8,4)
Veh6 = Motorcycle(1975,75500,40000,"bh545664rh",True)

#print(Veh1,Veh2,Veh3,Veh4,Veh5,Veh6)
#prints 	100000 	100001 	100002 	100003 	100004 	100005

# Veh7 = Motorcycle("year",10000,25000,"bjhgss4rdh",False)
# instance Veh7 generates an exception (ValueError) (uncomment to test)
