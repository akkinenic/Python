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

    # def __init__(self, customer, account, bank, limit,balance):
    #     self.customer = customer
    #     self.bank = bank
    #     self.account = account
    #     self.balance = balance
    #     self.limit = limit

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
        self.balance -=amount


"""
R-2.6 If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.
"""

#ANSWER - REFER TO LINES 96-99

"""
R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new account
to zero. Modify that class so that a new account can be given a
nonzero balance using an optional fifth parameter to the constructor. The
four-parameter constructor syntax should continue to produce an account
with zero balance.
"""

#ANSWER - REFER TO LINES 62-67

"""
R-2.8 Modify the declaration of the first for loop in the CreditCard tests, from
Code Fragment 2.3, so that it will eventually cause exactly one of the three
credit cards to go over its credit limit. Which credit card is it?
"""


#if __name__ == __main__ :
wallet = [ ]
wallet.append(CreditCard( 'John Bowman ', 5391037593875309, 'California Savings'  , 2500) )
wallet.append(CreditCard( 'John Bowman ', 3485039933951954, 'California Federal'   , 3500) )
wallet.append(CreditCard( 'John Bowman' ,5391037593875309, 'California Finance',  5000) )

for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2*val)
    wallet[2].charge(3*val)

for c in range(3):
    print( "Customer = ", wallet[c].get_customer())
    print( "Bank = ", wallet[c].get_bank())
    print( "Account =" , wallet[c].get_account( ))
    print( "Limit = ", wallet[c].get_limit( ))
    print( "Balance =" , wallet[c].get_balance())

while wallet[c].get_balance() > 100:
    wallet[c].make_payment(100)
   # print( "New balance = ", wallet[c].get_balance())
   # print( )


"""
R-2.9 Implement the sub method for the Vector class of Section 2.3.3, so
that the expression u−v returns a new vector instance representing the
difference between two vectors."""


def sub(self, other):
    if len(self) != len(other): # relies on len method
        raise ValueError( "dimensions must agree ")
        #result = Vector(len(self)) # start with vector of zeros
    #for j in range(len(self)):
        #result[j] = self[j] - other[j]
        #return result

"""
R-2.10 Implement the neg method for the Vector class of Section 2.3.3, so
that the expression −v returns a new vector instance whose coordinates
are all the negated values of the respective coordinates of v.
"""

# commented the code below because of IDE

#def neg(self):
    # result = Vector(len(self)) # start with vector of zeros
    # for j in range(len(self)):
    #     result[j] = ~self[j]
    #     return result

"""
R-2.11 In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector."""


#PLEASE REFER VECTOR.py

"""
R-2.12 Implement the mul method for the Vector class of Section 2.3.3, so
that the expression v 3 returns a new vector with coordinates that are 3
times the respective coordinates of v.
"""

#PLEASE REFER VECTOR.py


"""
R-2.13 Exercise R-2.12 asks for an implementation of mul , for the Vector
class of Section 2.3.3, to provide support for the syntax v 3. Implement
the rmul method, to provide additional support for syntax 3 v."""


#PLEASE REFER VECTOR.py
