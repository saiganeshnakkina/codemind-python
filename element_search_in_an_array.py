n=int(input())
lst=list(map(int,input().split()))
x=int(input())
cnt=0
for i in range(n):
    if lst[i]==x:
        cnt=True
if cnt==True:
    print(True)
else:
    print(False)
    