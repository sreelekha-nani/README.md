def factorial_recursion(n):
    if n<0:
        return factorial is not defined
    if n==0:
        return 1
    else:
        return n*factorial_recursion(n-1)
n=int(input("enter a number:"))
result=factorial_recursion(n)
print(f"The factorial of{n} is {result}")
