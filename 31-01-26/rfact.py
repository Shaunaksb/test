def rfact(n):
    if n==1:
        return 1
    else: 
        return n*rfact(n-1)

print(rfact(5))