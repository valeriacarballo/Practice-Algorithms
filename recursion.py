
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def fibRecursive (n: int):
    # base case - terminating/returning case (needs to know when to stop) ; usually if statement
    if n==0:
        return 0
    if n==1:
        return 1
    
    return fibRecursive(n-1) + fibRecursive(n-2)
    
    
print(fibRecursive(38)) #expected output: 55

