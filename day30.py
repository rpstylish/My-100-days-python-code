# factorial (7)= 7*6*5*4*3*2*1
# factorial (6)= 6*5*4*3*2*1
# factorial (5)= 5*4*3*2*1
# factorial (4)= 4*3*2*1
# factorial (0) = 1
# factorial (n) = n * factorial(n-1)

def facctorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * facctorial(n-1)
print(facctorial(3))
print(facctorial(4))
print(facctorial(5))


def fib(n):
    if(n==1 or n==2):
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(5))    