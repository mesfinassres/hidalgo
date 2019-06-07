import math
def printHello():
    print ("Hello")

def isPrime(n):
    isPrime = True
    for i in range(2, int(math.sqrt(n))):
        if n%i == 0:
            isPrime = False
    return isPrime

def printEven(n):
    for i in range(0, n):
        if i%2 == 0:
            print (i, " is even.")
        else:
            print (i, " is odd")    

print(isPrime(11))
