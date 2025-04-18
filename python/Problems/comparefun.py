                                # write a function to find greatest
def compare(a,b,c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    elif(c>a and b<c):
        return c
a=int(input("enter the num:"))
b=int(input("enter the num:"))
c =int(input("enter the num:"))
d=compare(a,b,c)
print(d)