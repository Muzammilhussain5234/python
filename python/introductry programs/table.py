n=int(input("enter a number whose table u want"))
table=[n*i for i in range(1,11)]
with open("2.txt","a") as f:
    f.write(f"table of {n} : {str(table)}\n")