import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([1,-1,0])
you=input("Enter the value s,w and g:")
dictionary={
    "s":1,"w":-1,"g":0
}
chose=dictionary[you]
print(f"you chose {chose} computer {computer}")
if(computer== chose):
    print("its a draw")
else:
    if(computer==-1 and chose==1):
      print("you win!")
    elif(computer==-1 and chose==0):
      print("you lose!")
    elif(computer==1 and chose==-1):
      print("you lose!")    
    elif(computer==-1 and chose==0):
      print("you win!")
    elif(computer==0 and chose==-1):
      print("you win!")    
    elif(computer==0 and chose==1):
      print("you lose!")  
    else:
      print("something wrong")
   
