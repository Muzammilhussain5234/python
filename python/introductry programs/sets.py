# i think the use of set is same as list or dictionary but it does not repeat tge same entities,they are unordered
set=set()
print(type(set))
# methods of sets
s={1,22,2,3,4,2}
s.add(7)
print(s,type(s))
s.remove(2)
print(s,type(s))
# {1, 3, 4, 22, 7} <class 'set'> output                    pop()
s.pop()
print(s,type(s))
#                                     union and intersection
s1={0,3,4,5,6,7,}
s2={1,2,8,4,3,2}
u=s1.union(s2)
v=s1.intersection(s2)
print(u)
print(v)
