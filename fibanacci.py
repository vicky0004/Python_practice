
n = int(input("Enter the number of digits that you want in the Fibonacci sequence: "))

n1, n2 = 0, 1

count = 0

if n <= 0:

    print("The input is invalid. Please enter a positive integer.")

elif n == 1:

    print("Fibonacci sequence up to n terms will be: ")

    print(n1)

else:
    print("Fibonacci sequence up to the given terms will be: ")

    while count < n:

        print(n1)

        nth = n1 + n2

        n1 = n2

        count = count + 1
