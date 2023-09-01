#question 2
print("1.convert kelvin temp to celcius and fahrenheit")
print("2.convert celcius temp to kelvin and fahrenheit")
print("3.convert fahrenheit temp to celcius and kelvin")

h=int(input("enter choice"))
if h==1:
    n=int(input("enter temp in kelvin"))
    print("temp in celcius is",(n-273))
    print("temp in fahrenheit is",(9/5*(n-273))+32)
elif h==2:
    n=int(input("enter temp in celcius"))
    print("temp in kelvin is",n+273)
    print("temp in fahrenheit is",((9/5)*n)+32)
elif h==3:
    n=int(input("enter temp in fahrenheit"))
    print("temp in celcius is",(n-32)*(5/9))
    print("temp in kelvin is",((n-32)*(5/9)+273))
else:
    print("wrong choice")
    
