from vehicle import *
from customer import *

class Employee(object):
    ######## CODE MISSING HERE
    emp_id = 0

    def __init__(self, name):
        pass
    ######## CODE MISSING HERE
        self.__name = name
        self.__id = Employee.emp_id
        Employee.emp_id += 1

    def __str__(self):
        pass
    ######## CODE MISSING HERE
        return 'Employee: ' + self.get_name() + ' is of type ' + self.get_title()


    def get_name(self):
        pass
    ######## CODE MISSING HERE
        return self.__name

    def get_title(self):
        pass
    ######## CODE MISSING HERE
        return 'Subordinate'

class Manager(Employee):

    def get_title(self):
        pass
    ######## CODE MISSING HERE
        return 'Manager'

    def get_sales_report(self,salesman):
        pass
    ######## CODE MISSING HERE
        try:
            return print(salesman.get_name()+ "'s current cumulative sales:\n" + str(Salesman.sales[salesman.get_name()]))
        except KeyError:
            return print(salesman.get_name() + ' is not in sales yet.')
class Salesman(Employee):

    ######## CODE MISSING HERE
    sales = {}

    def sale(self,vehicle,sales_price,customer):
        pass
    ######## CODE MISSING HERE

        if customer.credit_score() == True:
            if self.get_name in Salesman.sales.keys():
                Salesman.sales[self.get_name()] = Salesman.sales[self.get_name()] + sales_price
            else:
                Salesman.sales[self.get_name()] = sales_price

        else:
            print('The customer does not have enough credit score!')
### test cases ###

## initialising employee instances

Eric = Manager("Eric")
Kyle = Employee("Kyle")
Stan = Salesman("Stan")
Kenny = Salesman("Kenny")
Craig = Salesman("Craig")

## printing employee instances

# print(Eric) # expected output: Employee: Eric is of type Manager
# print(Kyle) # expected output: Employee: Kyle is of type Subordinate
# print(Stan) # expected output: Employee: Stan is of type Subordinate
# print(Kenny) # expected output: Employee: Kenny is of type Subordinate
# print(Craig) # expected output: Employee: Craig is of type Subordinate


## registering sales

Kenny.sale(Veh2,6000,Heidi)

# Stan.sale(Veh1,9000,Wendy)


## printing an individual sales report:

Eric.get_sales_report(Kenny)
# expected output:
# Kenny's current cumulative sales:
# 6000
