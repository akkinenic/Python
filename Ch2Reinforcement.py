"""
R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
"""


class Flower:

    def __init__(self,name,npetals,price):
        self._name = name
        self._npetals=npetals
        self._price=price

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_npetals(self):
        return self._npetals

    def set_npetals(self, value):
        self._npetals = value

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value

    def get_flower(self):
        return ("Name ->" + self.get_name() +" \n"
                                             "No of petals ->" +str(self.get_npetals()) +"\n"
                                                                              "Price ->"+str(self.get_npetals()))


flower = Flower("Rose",20,5.6)

print(flower.get_flower())


"""
R-2.5 Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter.
"""


class CreditCard:
    def __init__(self,customer,account,bank,limit):
        self.customer = customer
        self.bank=bank
        self.account=account
        self.balance=0
        self.limit=limit

    def get_customer(self):
        return self.customer

    def get_balance(self):
        return self.balance

    def get_account(self):
        return self.account

    def get_bank(self):
        return self.bank

    def get_limit(self):
        return self.limit

    def charge(self,price):
        if not isinstance( price, (int, float) ):
            raise TypeError( 'price must be numeric')
        elif price < 0:
            raise ValueError( 'price cannot be negative')
        if price + self.balance > self.limit:  # if charge would exceed limit,
            return False  # cannot accept charge
        else:
            self.balance += price
        return True

    def make_payment( self,amount ):
        if not isinstance( amount, (int, float) ):
            raise TypeError( 'amount must be numeric')
        elif amount < 0:
            raise ValueError( 'amount cannot be negative')
        self.bank -=amount