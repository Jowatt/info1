from vehicle import *


class Customer(object):
    
    def __init__(self,name):
        pass
    ######## CODE MISSING HERE

        self.__name = name
        self.__score = self.credit_score()

    def __str__(self):
        pass
    ######## CODE MISSING HERE

        return 'Customer: ' + self.__name


    def credit_score(self):
        pass
    ######## CODE MISSING HERE

        import random
        score = random.randint(0,100)
        if score > 60:
            return True
        else:
            return False

    def get_score(self):
        pass
    ######## CODE MISSING HERE

        return self.__score



class VIP_Customer(Customer):

    def credit_score(self):
        pass
    ######## CODE MISSING HERE

        return True

### test cases ###

# initialising customer instances

Wendy = Customer("Wendy")
Heidi = VIP_Customer("Heidi")

# print(Wendy) # expected output: Customer: Wendy
# print(Heidi) # expected output: Customer: Heidi

# print(Wendy.get_score()) # expected output: True
# print(Heidi.get_score()) # expected output: True
