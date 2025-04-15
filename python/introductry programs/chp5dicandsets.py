marks={
    "harry":100,
    "ali":55,
    "suneo":66

}
print(marks.items())
#  output   [('harry', 100), ('ali', 55), ('suneo', 66)])  it will give u tuples
print(marks.keys())
# ['harry', 'ali', 'suneo'] it will return me with element on left side
marks.update({"harry":99})
print(marks)
#                        get()
print(marks.get("harry"))
# output will be 99 bcz  of marks.update({"harry":99})
# print(marks)
# #                        get()
# print(marks.get("harry"))