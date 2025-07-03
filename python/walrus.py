if(n:=len([1,2,3,4,5]))>3:
    print(f"list is too long {n} elments ,expected <=3")

#types
n:int=5
m:str="haary"
def sum(a:int,b:int)->int:
    return a+b
print(sum(4,5))
print(type(sum(4,5)))