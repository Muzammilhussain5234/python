friend=["hanan","rehan","nouman","subhan"]
print(friend[3])
#                              a good thing about lists is we can make changes unlike strings
friend[3]="roman"
print(friend)            
# ['hanan', 'rehan', 'nouman', 'roman']


# function for lists
# sort( ) will arrange in increasing order
l1=[1,3,5,945,2,4]
l1.sort()
print(l1)
                # append add a number in the end number or string whatever u want
l1.append("chacha")
print(l1)
# reverse()
l1.reverse()
print(l1)
# insert(input,index)
l1.insert(3,4555)
print(l1)
# pop(index)
l1.pop(3)
print(l1)
# given ['chacha', 945, 5, 4555, 4, 3, 2, 1]
# answer ['chacha', 945, 5, 4, 3, 2, 1]
# remove()