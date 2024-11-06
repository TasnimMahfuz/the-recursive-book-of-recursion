def exponent_by_recursion(a,n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    
    elif n%2 == 0:
        result = exponent_by_recursion(a, n//2)
        return result*result
    
    elif n%2 == 1:
        result = exponent_by_recursion(a, n//2)
        return result*result*a
    
print(exponent_by_recursion(3,6))
print(exponent_by_recursion(10,3))
print(exponent_by_recursion(17, 10))