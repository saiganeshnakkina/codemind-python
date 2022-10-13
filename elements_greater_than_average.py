n=int(input())
x=list(map(int,input().split()))
a=sum(x)//n
c=0
for i in range(n):
    if a<=x[i]:
        c+=1
print(c)