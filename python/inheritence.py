class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."
class dog(animal):
    def characteristics(self,property):
        return f"{self.name} is loyal and {property}."
class anatomy(dog):
    def __init__(self, organ,specific_organ, name):
        self.organ = organ
        self.specific_organ = specific_organ
        # this code was created to show the use of of super() function
        super().__init__(name)   
    def show_anatomy(self):
        return f"This is the {self.specific_organ} of the {self.organ}."    
             
b=animal("buddy")
a=anatomy("heart", "left ventricle","buddy")
print(a.speak())                    
print(a.characteristics("friendly")) 
print(a.show_anatomy())   