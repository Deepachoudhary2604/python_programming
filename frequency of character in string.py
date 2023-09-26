a=input("enter string")
c=" "

for i in a:
    b=0
    if i not in c:
       c=c+i
       b=a.count(i)
       print(i,"  ",b)
    
    
