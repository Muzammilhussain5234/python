#                                 write a recursive function to add n num
def add(n):
    sum=(n*(n+1))/2
    return sum
a=int(input("enter the num:"))
d=add(a)
print(d)