n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
k=0
for i in x:
    if i>b or i<a:
        k+=i
print(k)