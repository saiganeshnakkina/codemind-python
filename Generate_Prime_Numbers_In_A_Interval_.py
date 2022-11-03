a=int(input())
b=int(input())
for i in range(a,b+1):
    n=0
    for j in range(1,i):
        if i%j==0:
            n+=1
    if n==1:
        print(i)