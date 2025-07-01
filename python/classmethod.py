class Language:
    language_name = "TypeScript"

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_language_name(cls):
        print(f"Class method called: Language is {cls.language_name}")


Language.show_language_name()
print(Language.language_name)
a = Language("JavaScript")
print(a.name)
print(a.language_name)
print(Language.language_name)
Language.show_language_name()
a.show_language_name()  


    