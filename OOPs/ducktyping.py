class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")


class Person:
    def speak(self):
        print("Hello")


def communicate(obj):
    obj.speak()


communicate(Dog())
communicate(Cat())
communicate(Person())