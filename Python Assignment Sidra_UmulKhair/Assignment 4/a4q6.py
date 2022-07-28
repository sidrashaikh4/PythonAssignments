class Animal:
    def Walk(self):
        print('Animal Walk')


class Dog(Animal):
    def Walk(self):
        print('dog Walk')


d = Dog()
d.Walk()

