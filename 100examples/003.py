# Script based python 3.7
import math

def isSquare(n):
    m = math.floor(math.sqrt(n))
    if m**2==n:
        return True
    else:
        return False
k = 0;
while(True):
    if isSquare(k+100) and isSquare(k+268):
        print(k)
        break
    k += 1
