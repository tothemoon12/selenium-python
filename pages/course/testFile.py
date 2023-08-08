class Person:
    def __init__(self, id, name):
        self.name = name
        self.id = id


p = Person(10, "Alik")

match(p):
    case Person(name=p):
        print("Alik")
    case _:
        print("not alik")
