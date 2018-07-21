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