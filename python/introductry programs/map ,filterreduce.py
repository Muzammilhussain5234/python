from functools import reduce
lis=[1,2,3,4,5,6]
sum= lambda a, b: a +b
print(reduce(sum,lis))
def filte(n):
   if(n%2==0):
    return True
   else:
     return False
print(list(filter(filte,lis)))
square=lambda x:x*x
print(list(map(square,lis)))
