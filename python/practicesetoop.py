class Employee:
    salary = 50000  
    increment = 5000
    @property
    def salary_after_increment(self):
        return self.salary +self.salary*(self.increment/100)
    @salary_after_increment.setter
    def salary_after_increment(self, salary):
        self.increment = ((salary/self.salary)-1) * 100
e=Employee()
print(e.salary_after_increment)   
e.salary_after_increment = 60000
print(e.increment)   
# probelm 2
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __mul__(self,other):
        return Complex(self.real * other.real - self.imag * other.imag, 
                       self.real * other.imag + self.imag * other.real)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __str__(self):
        return f"{self.real} + {self.imag}i"
c= Complex(2, 3)
d= Complex(4, 5)
print(c+d)
print(c*d)

