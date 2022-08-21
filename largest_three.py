
# Python program to find the largest

def maximum(x, y, z):

    if (x >= y) and (x >= z):

        largest = x

    elif (y >= x) and (y >= z):

        largest = y

    else:

        largest = z

    return largest

