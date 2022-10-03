n=int(input())
s=n*n
z=0
for i in str(s):
    z=z+int(i)
if(z==n):
    print("Neon Number")
else:
    print("Not Neon Number")