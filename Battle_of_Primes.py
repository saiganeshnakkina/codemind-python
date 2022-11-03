n1=int(input())
n2=int(input())
a=n1+n2
x=a
while True:
    a+=1
    c=0
    for i in range(1,a):
        if a%i==0:
            c+=1
    if c==1:
        print(a-x)
        break
    
        
    