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
