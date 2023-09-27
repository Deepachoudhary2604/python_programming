a=int(input("enter no."))
b=a
s=" "
while a:
    c=a%10
    s=s+str(c)
    a=a//10
if b==int(s):
    print("Palindrome")
else:
    print("not palindrome")
