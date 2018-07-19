#15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).


def distinctNums(data):
    newList = [ ]
    for i in range(0,len(data)):
        if not newList.__contains__( data[i] ):
            newList.append(data[i])
    return True if len(newList) == len(data) else False

print(distinctNums([1,1,2,3,5,6]))