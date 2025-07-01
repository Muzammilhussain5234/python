# class naming:
#     @property
#     def name(s):
#         return f"Name is {s.fname} and {s.lname}"
#     @name.setter
#     def name(s,value):
#         s.fname= value.split()[0]
#         s.lname = value.split()[1]
# c= naming()
# c.name = "John Doe"
# print(c.name)
# print(c.fname)
# print(c.lname)
class splitiing:
    @property
    def service(t):
        return f"Service is {t.fname} and {t.code}"
    @service.setter
    def service(t,name):
        t.fname = name.split()[0]
        t.lcode = name.split()[1]
s= splitiing()
s.service="service 225"
print(s.fname)
print(s.lcode)        
