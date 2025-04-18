#                              create a function to print a table
def table(num):
    for i in range(1,11):
        print(f"{num}X{i}={num*i}")
a=int(input("enter the num:"))
print(table(a))        
        