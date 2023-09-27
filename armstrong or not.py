a=int(input("enter no."))
c=0
r=0
q=a
p=a
while a:
    c=c+1
    a=a//10
while p:
    b=p%10
    r=r+b**c
    p=p//10
if q==r:
    print("armstrong")
else:
    print("not")
    
