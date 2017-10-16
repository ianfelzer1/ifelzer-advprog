startNumber = int(raw_input("Enter starting number here"))
endNumber = int(raw_input("Enter fininshing number here"))

# xn = xn-1 + xn-2
def fib(n):
    if n > 0:
        return n
        return fib(n-2) + fib(n-1)

print map(fib, range(startNumber,endNumber))

        
