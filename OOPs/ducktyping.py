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


class Pen:
   def use(self):
       return "Writing"
class Eraser:
   def use(self):
       return "Erasing"
def perform_task(tool):
   print(tool.use())
perform_task(Pen())
perform_task(Eraser())