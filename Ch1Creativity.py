""" 13 Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing. """


def reversee(data):
   return [data[i] for i in range(len(data)-1,-1,-1)]


def reverseList(data):
    return [data[-(i+1)] for i in range(len(data))]


print(reverseList([1,2,3,4,5]))

print(reversee([1,2,3,4,5]))


""" 14 Write a short Python function that takes a sequence of integer values and
 determines if there is a distinct pair of numbers in the sequence whose
 product is odd. """


def distinctPair(data):    #A product of two numbers will be odd both of the numbers are odd
    newList = []
    #newList = [data[i] for i in range(0,len(data)) if ((data[ i ] & 1) and (not newList.__contains__( data[i] )))]
    for i in range( 0, len( data ) ):
        if data[ i ] & 1 and not newList.__contains__( data[ i ] ):
            newList.append(data[i])
            if len(newList) > 1 :        #don't have to loop through all the numbers after u find a distinct pair
                return True
    return False


print(distinctPair([1,1,2,3,5,6]))

""" 15 Write a Python function that takes a sequence of numbers and determines
 if all the numbers are different from each other (that is, they are distinct). """


def distinctNums(data):
    newList = [ ]
    for i in range(0,len(data)):
        if not newList.__contains__( data[i] ):
            newList.append(data[i])
    return True if len(newList) == len(data) else False


print(distinctNums([1,1,2,3,5,6]))


def is_distinct(data):
    list = len(data)
    set = len(set(data)) #set actually consists of distinct objects
    return True if list == set else False


""" 16 1.16 In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] = factor. We have discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller? """

#def scale(data, factor):
#for j in range(len(data)):
#data[j] = factor


#Answer - The data is the formal parameter that is just an alias to the actual list.
#Hence, when we make scale changes, the actual list value gets changed making our scale function work properly.


""" 17 Had we implemented the scale function (page 25) as follows, does it work
 properly?
def scale(data, factor):
for val in data:
val = factor
Explain why or why not. """


#Answer - It will not work properly. This is because val is not an alias to the actual data value.
#This assignment simply creates a new val object


""" 18 Demonstrate how to use Python’s list comprehension syntax to produce
 the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]."""

list = [i*(i+1) for i in range(10)]

print(list)


#Hard Way that will not give points


def compute():
    newlist=[]
    val = 0
    for i in range(10):
        if(i<2):
            newlist.append(2*i)
            val = 2*i
        else:
            val = val + 2 * i
            newlist.append(val)
    return newlist


print(compute())


""" 19 Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
 characters literally. """

list=[chr(i) for i in range(97,123)] #instead of passing 97,123 - we can pass ord('a'), ord('z')+1
print(list)

""" 20 Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function. """


def myShuffle(data):
    from random import randint
    m = randint(0,len(data)-1)
    n = randint(0,len(data)-1)
    data[m],data[n] = data[n], data[m]
    return data


print(myShuffle([1,2,3]))



"""21 Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D)."""

newList = []
print("ENTER LINES. END OF FILE WITH CTRL+D")
try:
    while True:
        newList.append(input())
except EOFError:
    print("END OF FILE")
    newList.reverse()
    for i in newList:
        print(i)


"""22 Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . ,n−1."""


def dot_product(a,b):
    assert len(a) == len(b)
    output = [a[i]*b[i] for i in range(len(a))]
    return output


a=[1,2,3,4]
b=[5,6,7,8]
print(dot_product(a,b))

"""C-1.23 Give an example of a Python code fragment that attempts to write an element
to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!” """


try:
    a = [1,2,3]
    for i in range(len(a)+1):
        a[i] = 2
except IndexError:
    print('"Don’t try buffer overflow attacks in Python!"')


"""C-1.24 Write a short Python function that counts the number of vowels in a given
character string."""


def count_vowels(input):
    list = ['a','e','i','o','u']
    count = 0;
    for i in input:
        if list.__contains__(i):
            count +=1
    return count


print(count_vowels("standard"))


"""C-1.25 Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example,
if given the string "Let s try, Mike.", this function would return
"Lets try Mike"."""


def remove_punctuation(string):
    outputstring = str()
    for a in string:
        if a.isalpha() or a == ' ':
            outputstring +=a
    return outputstring


print(remove_punctuation("Let s try, Mike."))


"""C-1.26 Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”"""

str = input("Enter three integers , seperated").split(",")
a,b,c = (int(i) for i in str)
print("{} + {} = {} ?".format(a, b, c), a + b == c)
print("{} = {} - {} ?".format(a, b, c), a == b - c)
print("{} = {} * {} ?".format(a, b, c), a == b * c)

"""27 C-1.27 In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementations,
from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance advantages."""


def factors(n): # generator that computes factors
    k = 1
    result = []
    while k*k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            result.append(n // k)
        k += 1
    if k*k == n: # special case if n is perfect square
        yield k
    result.reverse()
    for i in result:
        yield i


print(list(factors(100)))