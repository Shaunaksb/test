def rfib(n):
    if n==1:
        return(1)
    else:
        return n+rfib(n-1)

print(rfib(5))