
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
