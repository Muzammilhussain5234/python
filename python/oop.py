# class sodium:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Sodium: {self.name}"
# metal=sodium("Na")
# print(metal)
# metal.name = "Sodium"
# print(metal)
# problem 1
# class programmer:
#     company="micarosoft"
#     def __init__(t,name,salary,pin):
#         t.name=name
#         t.salary=salary
#         t.pin=pin
# h=programmer("spidey",100000,1234)     
# H=programmer("hulk",100000,1234)  
# print(h.name,h.salary,h.pin,h.company)
# print(H.name,H.salary,H.pin,H.company)
# problem 2
# class calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b  
#     def sub(self):
#         return self.a - self.b
#     def mul(self):
#         return self.a * self.b
#     def div(self):
#         if(self.b==0):
#             return "Division by zero is not allowed"
#         else:
#             return self.a / self.b
# cal=calculator(10, 5)  
# print(f"addition:{cal.add()}  subtraction:{cal.sub()} multiplication:{cal.mul()} division:{cal.div()}")  
# problem 3
# class greeting:
#     @staticmethod
#     def salam():
#         return "Assalamualaikum"
# s=greeting()
# print(s.salam())    
                                                     # problem 4
class train:
    def __init__(c,trainno):
        c.trainno = trainno
    def book(c,name,fro,to):
        print(f"ticket booked for {name} from {fro} to {to} in train number {c.trainno}")
    def status(c):
        print(f"status of train {c.trainno} is running")
    def fare(c,fare):
        print(f"fare for train {c.trainno} is {fare}")
t=train(12345)
t.status()
t.fare(2000)
t.book("spidey", "lahore", "rawalpindi")
  
        