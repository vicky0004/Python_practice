
def calc_hcf(x, y):


    if x > y:

        smaller = y

    else:

        smaller = x

    for i in range(1, smaller + 1):

        if ((x % i == 0) and (y % i == 0)):

            hcf = i

        return hcf

num1 = int(input ("Enter the first number as required: "))

num2 = int (input ("Enter the second number to find the HCF: "))

print ("The HCF of the two numbers entered is", calc_hcf (num1, num2))
