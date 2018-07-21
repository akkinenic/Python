"""29 P-1.29 Write a Python program that outputs all possible strings formed by using
#the characters c , a , t , d , o , and g exactly once."""

#method 1


def permute_helper(str,chosen=""):
    if str == "":
        print(chosen)
        return chosen
    else:
        for a in str:
            """ choose"""
            pull = a
            chosen +=pull
            str = str.replace(a,"")
            """explore"""
            permute_helper(str,chosen)
            """un-choose"""
            str +=pull
            chosen = chosen.replace(pull,"")

def permute(str):
    permute_helper(str)

#print(permute("catdog"))

#method 2


def permutations(word):
    if len( word ) == 1:
        return [ word ]

    # get all permutations of length N-1
    perms = permutations( word[ 1: ] )
    char = word[ 0 ]
    result = [ ]
    # iterate over all permutations of length N-1
    for perm in perms:
        # insert the character into every possible location
        for i in range( len( perm ) + 1 ):
            result.append( perm[ :i ] + char + perm[ i: ] )

    return result


#print(permutations( "catdog" ))

"""
P-1.30 Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""


def count_divby2(val):
    count = 0
    if val == 2:
        return 1

    if val < 2:
        return 0

    while val >= 2:
        val = val//2
        count +=1
    return count

print(count_divby2(9))

"""
P-1.31 Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
"""


def make_change(charged,given):
    denominations = [.01,.05,.1,.25,1,5,10,20,50,100]
    return_money = given-charged
    a=b=0
    isBill=False
    for i in range(len(denominations)):
        if a > 0:
            if isBill:
                print( denominations[ -i ], "$ bills delivered", int(a) )
            else:
                print( denominations[ -i ], " coins delivered", int(a) )
        if return_money > 0:
            isBill = True if return_money >=1 else False
            a,b = divmod(return_money,denominations[-(i+1)])
            return_money = b
        else:
            break


make_change(2,103.5)


"""
P-1.32 Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
"""


def calculator():
    inp1 = input("Enter first input\n")
    inp2 = input("Enter second input\n")

    op = input("Enter Operator\n")

    if op == "+":
        print(inp1+"+"+inp2+"=")
        print(inp1+ inp2)
    elif op == "-":
        print(inp1+"-"+inp2+"=")
        print(inp1 - inp2)

    elif op == "*":
        print(inp1+"*"+inp2+"=")
        print(inp1 * inp2)
    else:
        print("Invalid Entry")


#calculator()

"""
P-1.33 Write a Python program that simulates a handheld calculator. Your program
should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each operation
is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation."""

#DID NOT GET A CHANCE TO IMPLEMENT

"""
P-1.34 A common punishment for school children is to write out a sentence multiple
times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
"""


def punishment():
    content = {}
    for i in range(1,101):
        content[ i ] = "I will never spam my friends again."
    from random import randrange
    for i in range(1,9):
        content[randrange(1,100)] = "I got a  typo"
    from pprint import pprint
    pprint(content)


#punishment()


"""
P-1.35 The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100.
"""


def test_birthday(n):
    from random import randint
    from itertools import groupby
    random_birthdays = [randint(1,31) for ele in range(n)]
    print(random_birthdays)
    frequency_ = [ len( list( group ) ) for key, group in groupby( random_birthdays ) ]
    count = 0
    for ele in frequency_:
        if ele > 1:
            count += 1
    return "Two people in a room have same birthday" if count > 0 else "Two people in a room do not have same birthday"


print("5 people group -->"+ str(test_birthday(5)))
print("5 people group -->"+ str(test_birthday(10)))
print("5 people group -->"+ str(test_birthday(15)))
print("5 people group -->"+ str(test_birthday(20)))
print("5 people group -->"+ str(test_birthday(25)))
print("5 people group -->"+ str(test_birthday(30)))
print("5 people group -->"+ str(test_birthday(35)))
print("5 people group -->"+ str(test_birthday(40)))
print("5 people group -->"+ str(test_birthday(45)))
print("5 people group -->"+ str(test_birthday(50)))
print("5 people group -->"+ str(test_birthday(55)))


"""
P-1.36 Write a Python program that inputs a list of words, separated by whitespace,
and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.
"""


def word_counter():
    from collections import Counter
    data = input("Input the list of words\n").split(" ")
    content = {}
    for a in data:
        if content.__contains__(a):
            content[a] +=1
        else:
            content[a] = 1
    from pprint import pprint
    pprint(content)

word_counter()