#question 6
n=int(input("enter no. of seconds"))
hours=n//3600             
s=n-(hours*3600)
minutes=s//60
t=s-(minutes*60)
print(hours,"hours",minutes,"minutes",t,"seconds")
