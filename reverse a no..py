a=int(input("enter n0."))
s=" "
while a:
    c=a%10
    s=s+str(c)
    a=a//10
print(s)
