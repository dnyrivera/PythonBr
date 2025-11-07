class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self) -> None:
        print("Au au au")


class cat(Animal):
    def sound(self) -> None:
        print("Miau Miau")


# Polimorphism
animal = Animal()
dog = Dog()
cat = cat()

animal.sound()
dog.sound()
cat.sound()
