##list(range(5,10))
#print("hello")
#for i in range(1, 10):
#    print (i)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

import math
def isPrime(n):
    isPrime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            isPrime = False
            break
    return isPrime

def isSemiprime(n):
    count = 0
    for i in range(2, int(math.sqrt(n)) +1):
        while n%i == 0:
            n /=i
            count +=1
        if count > 2:
            break
    if n>1:
        count +=1
    return count == 2

def insertionSort(A):
    n = len(A)
    for i in range(0, n):
        j = i
        done = False
        while j>= 1 and not done:
            if A[j] < A[j-1]:
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
                j -= 1
            else:
                done  = True
    return A    
        
x = Node(5)
print(x.data)
print("prime", isPrime(17))
print("semi prime", isSemiprime(4))
print("Sort", insertionSort([9,4,5,3,2,6]))
print("Sort", insertionSort(['F','B','D','A','C','E']))