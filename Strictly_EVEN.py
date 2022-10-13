n=int(input())
x=list(map(int,input().split()))
y=[]
z=[]
for i in range(len(x)):
    if x[i]%2==0 and i%2==0:
        y.append(x[i])
    else:
        z.append(x[i])
for j in z:
    if j%2==0:
        print("False")
        break
else:
    print("True")