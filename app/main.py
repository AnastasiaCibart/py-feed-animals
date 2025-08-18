from typing import List


class Animal:
    def __init__(self, name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name: str = name
        self.appetite: int = appetite
        self.is_hungry: bool = is_hungry

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> str:
        print("The slippers delivered!")


def feed_animals(animals: List[Animal]) -> int:
    total_appetite: int = 0
    for animal in animals:
        total_appetite += animal.feed()
    return total_appetite


cat = Cat("Cat", False)
lion = Animal("Lion", 25, True)
dog = Dog("Dog")

print(feed_animals([cat, lion, dog]) == 32)
print(dog.bring_slippers())
print(cat.catch_mouse())
