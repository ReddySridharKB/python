# Single Inheritance
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Dog is barking...")

dog = Dog()
dog.eat()
dog.bark()


# Multiple Inheritance
print("------------------")

class Father:
    def skills(self):
        print("Father : Gardening, Programming")

class Mother:
    def skills(self):
        print("Mother : Cooking, Art")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child : Sports")

child = Child()
child.skills()

# Multilevel Inheritance
print("------------------")

class Animal:
    def eat(self):
        print("Animal is eating")


class Mammal(Animal):
    def walk(self):
        print("Mammal is walking")


class Dog(Mammal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.walk()
dog.bark()

# Hierarchical Inheritance
print("------------------")

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()

# Hybrid Inheritance
print("------------------")
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


class Pet(Dog, Cat):
    def play(self):
        print("Pet is playing")


pet = Pet()

pet.eat()
pet.bark()
pet.meow()
pet.play()