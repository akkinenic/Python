#Reinforcement Solutions


#1 Write a short Python function, is multiple(n, m), that takes two integer
#values and returns True if n is a multiple of m, that is, n = mi for some
#integer i, and False otherwise.


def is_multiple(n,m):
    return True if n%m==0 else False


n = int(input("Enter n"))
m = int(input("Enter m"))

print(is_multiple(n,m))


#2   Write a short Python function, is even(k), that takes an integer value and
#   returns True if k is even, and False otherwise. However, your function
#   cannot use the multiplication, modulo, or division operators.


def is_even(k):
    return 'Odd' if(k & 1) else 'Even'


k = int(input("Enter k"))

print(is_even(k))


#3   Write a short Python function, minmax(data), that takes a sequence of
#    one or more numbers, and returns the smallest and largest numbers, in the
#    form of a tuple of length two. Do not use the built-in functions min or
#    max in implementing your solution.

def minmax(data):
    max = min = data[0]
    for val in data:
        if val > max:
            max = val
        if val < min:
            min = val
    return max,min


numbers = (input(print("Enter numbers ',' seperated")))

max,min = minmax(list(map(int, numbers.split(','))))

print("Maximum is ", max)

print("Minimum is ", min)


#4 Write a short Python function that takes a positive integer n and returns
#  the sum of the squares of all the positive integers smaller than n.

def sum_squares(n):
    sum = 0
    i = 1
    while i in range(1,n):
        sum +=i*i
        i += 1
    return sum

question = int(input("Enter n to get sum of squares"))

print("Result is ", sum_squares(question))

#5 Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.

questionNew = int(input("Enter n to get sum of squares"))

print("Result is ", sum(i*i for i in range(1,questionNew)))

#6 Write a short Python function that takes a positive integer n and returns
#  the sum of the squares of all the odd positive integers smaller than n.


def sum_squares_odd(n):
    sum = 0
    i = 1
    while i in range(1,n):
        if (i % 2 == 1):
            sum += i*i
        i += 1
    return sum


question6 = int(input("Enter n to get sum of squares of odd numbers"))

print("Result is ", sum_squares_odd(question6))

#7 Give a single command that computes the sum from Exercise R-1.6, relying
#  on Python’s comprehension syntax and the built-in sum function.

question7 = int(input("Enter n to get sum of squares of odd numbers"))

print("Result is ", sum(i*i for i in range(1,question7) if i%2 == 1))


#8 Python allows negative integers to be used as indices into a sequence,
#such as a string. If string s has length n, and expression s[k] is used for index
#−n≤k<0, what is the equivalent index j ≥0 such that s[j] references
#the same element?

givenString = input("Enter String")
negIndex = int(input("Enter -ve index. Please add '-' to the integer"))
print(True if givenString[negIndex] == givenString[len(givenString)+negIndex] else False)
print("Equivalent +ve index", len(givenString)+negIndex)


#9 What parameters should be sent to the range constructor, to produce a
#range with values 50, 60, 70, 80?

for i in range(50,90,10):
    print(i)

#10 What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

for i in range(8,-10,-2):
    print(i)


#11 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

list = [2**i for i in range(9) ]
print(list)

#12 Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes
# a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.

def myChoice(data):
    from random import randrange
    return data[randrange(len(data))]
print(myChoice([1,2,3,4,5]))
