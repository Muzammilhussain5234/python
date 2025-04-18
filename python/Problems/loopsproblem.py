#                                   multiplication of a table
# a=int(input("enter a number u want the table:"))
# for i in range(1,11):
#     print(f"{a}X{i}={a*i}")
#                                make a program containiing a specific letter from a list
# li=["hero ","hamada","shezan","rohan"]
# for name in li:
#     if(i.startswith("s")):
#         print(f"hello {name}")
#                                 multiplication of table using while
# a=int(input("enter a number u want the table:"))
# i=1
# while(i<11):
#    print(f"{a}X{i}={a*i}")
#    i+=1                        
#                                  check the num is prime or not by loops
# n=int(input("enter a number u want to check:"))
# for i in range(2,n):
#     if(n%i)==0:
#         print("number is not prime")
#         break
# else:
#     print("number is prime")
#                             5  sum of n numbers using while loop

# i=1
# sum=0
# n=int(input("enter a number u want to check:"))
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)
                                # 6 factorial find
# n=int(input("enter a number u want to check:"))
# product=1
# for i in range(1,n+1):
#    product=product*i
# print(f"factorial of {n} is {product}")
#                    print star in triangular form

# n=int(input("enter a number u want stars:"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")
#                                  Print stars in right angle triangle
# n=int(input("enter a number u want stars:"))
# for i in range(1,n+1):
#     print("*"*(2*i-1),end="")
#     print("")
#                                  print stars and make a pattern as hollow square
# n=int(input("enter a number u want stars:"))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")                
#                                  Print table in reverse order
a=int(input("enter a number u want the table:"))
for i in range(1,11):
  print(f"{a}X{11-i}={a*(11-i)}")