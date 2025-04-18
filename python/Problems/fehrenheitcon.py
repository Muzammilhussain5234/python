
#                                 write a function to convert fahrenheit to celsius
def celtofeh(f):
    c=5*(f-32)/9
    return c
f=int(input("enter the num:"))
d=celtofeh(f)
print(f"the celsius is {d}")