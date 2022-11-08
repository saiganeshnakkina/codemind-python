n=int(input())
s=len(str(n))
square=n**2
r=square%pow(10,s)
if r==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')