name="Muzammil"
newname=name[0:5]
print(newname)
print(name[-6:-3])
print(name[3:6])

# other cases of string
new="abcdefghijklmnopqrstuvwxyz"
print(new[5:23:7])

# answer=fmt
# for finding the length of string
print(len(new))
# answer=26
# finding specific character ARE PRESENT or not
print(new.endswith("xyz"))
# answer=true
# another
print(new.startswith("xyz"))
# false
print(new.capitalize())
# only return first letter of string
print(new.find("x"))
# this will retrun the index that startwith
print(new.replace("xyz","python"))
# this will replace and we get answer
# abcdefghijklmnopqrstuvwpython 
                                #    splitter
text2="1,2,3,4"
print(text2.split(","))
# ['1', '2', '3', '4'] answer