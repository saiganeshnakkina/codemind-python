n=int(input())
x=False
if n>1:
    for i in range(2,n):
        if n%i==0:
            x=True
            break
    if x:
        print('not a prime')
    else:
        print('prime')
        