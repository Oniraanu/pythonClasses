class Animal:
    def __init__(self, name, age=0):
        print("From Animal")
        self.name = name
        self.age = age

    def speak(self):
        return "Animal speak"


class Dog(Animal):
    def __init__(self, name, age, type_):
        print("From Dog")
        super().__init__(name, age)
        self.type = type_

    def speak(self):
        super().speak()
        return "Dog Speak"


class Cat(Animal):
    pass


dog = Dog("Bingo", 2, "Local")
cat = Cat("Kitty")

print(dog.speak())
print(dog.name)
print(dog.type)
print(dog.speak())
