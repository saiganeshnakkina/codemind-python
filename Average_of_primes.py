def isprime(a):
    if a==1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
    
n=int(input())
arr=list(map(int,input().split()))
c=[]
for i in arr:
    if isprime(i)>=1:
        c.append(i)
b=len(c)
d=(sum(c)/b)
print("%.2f"%d)