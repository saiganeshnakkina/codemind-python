a=int(input())
b=int(input())

for i in range(a,b+1):
    s=i
    while i>0:
        r=i%10
        if r==0 or s%r!=0:
            break
        i=i//10
        
    else:
        print(s,end=' ')