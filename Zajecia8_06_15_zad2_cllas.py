class Person:
    def __init__(self, name):
        self.__name = name


    @property
    def name(self):
        print("pobieram imie")
        return self.__name


    @name.setter
    def name(self, value):
        """Setter – ustawia nowe saldo z walidacją"""
        if not isinstance(value, str):
            raise ValueError("To musi byc string")
        self.__name = value

p=Person("Alicja")
print(p.name)


p.name="Janek"
print(p.name)

p.name=123
print(p.name)