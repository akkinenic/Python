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



