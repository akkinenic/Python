#13 Write a pseudo-code description of a function that reverses a list of n
#integers, so that the numbers are listed in the opposite order than they
#were before, and compare this method to an equivalent Python function
#for doing the same thing.


def reversee(data):
   return [data[i] for i in range(len(data)-1,-1,-1)]


def reverseList(data):
    return [data[-(i+1)] for i in range(len(data))]


print(reverseList([1,2,3,4,5]))

print(reversee([1,2,3,4,5]))


#14 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.


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

#15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).


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


#16 1.16 In our implementation of the scale function (page 25), the body of the loop
#executes the command data[j] = factor. We have discussed that numeric
#types are immutable, and that use of the = operator in this context causes
#the creation of a new instance (not the mutation of an existing instance).
#How is it still possible, then, that our implementation of scale changes the
#actual parameter sent by the caller?

#def scale(data, factor):
#for j in range(len(data)):
#data[j] = factor


#Answer - The data is the formal parameter that is just an alias to the actual list.
#Hence, when we make scale changes, the actual list value gets changed making our scale function work properly.


#17 Had we implemented the scale function (page 25) as follows, does it work
#properly?
#def scale(data, factor):
#for val in data:
#val = factor
#Explain why or why not.


#Answer - It will not work properly. This is because val is not an alias to the actual data value.
#This assignment simply creates a new val object


#18 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

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

