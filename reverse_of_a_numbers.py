x=int(input())
s=0
while x>0:
    r=x%10
    s=s+r
    print(r,end='')
    x=x//10