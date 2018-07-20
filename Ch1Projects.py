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

print(permute("catdog"))

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


print(permutations( "catdog" ))

"""
P-1.30 Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""

