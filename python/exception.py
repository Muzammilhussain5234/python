try:
    a=int(input("enter a num"))
    print(a)
except Exception as e:
    print(e)    
    
else:
    print("u r good to go")    


#try finally
try:
    a=int(input("enter a num"))
    print(a)
except Exception as e:
    print(e)    
    
finally:
    print("u r good to go")     