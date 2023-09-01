#question 8
n1=int(input("enter first side"))
n2=int(input("enter second side"))
n3=int(input("enter third side"))
s=(n1+n2+n3)/2
area=(s*(s-n1)*(s-n2)*(s-n3))**(1/2)
print(area)
