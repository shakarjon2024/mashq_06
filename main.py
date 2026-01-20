class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [
    Person("Ali", 20),
    Person("Vali", 30),
    Person("Sami", 17)
]

adults = [p.name for p in people if p.age >= 18]
print("Voyaga yetganlar:", adults)
