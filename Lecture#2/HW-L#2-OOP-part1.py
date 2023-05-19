class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating! It is animal!")

    def sleep(self):
        print(f"{self.name} is sleeping! It is animal!")

    def paws(self):
        print(f"{self.name} has four paws.")


class Cat(Animals):
    def noise(self):
        print(f"{self.name} makes meow!!!")


cat = Cat("Kitty")
cat.noise()


class Dog(Animals):
    def noise(self):
        print(f"{self.name} barking!!!")


dog = Dog("Rocky")
dog.noise()


class Cow(Animals):
    def noise(self):
        print(f"{self.name} makes - mooooo!!!")


cow = Cow("Zorka")
cow.noise()


class Snake(Animals):
    def noise(self):
        print(f"{self.name} makes - shhhhhhhhh!!!")

    def paws(self):
        print(f"{self.name} has no paws. It is snake!")


snake = Snake("Focus")
snake.noise()
snake.paws()


class Duck(Animals):
    def fly(self):
        print(f"{self.name} can fly!")

    def paws(self):
        print(f"{self.name} has 2 paws. It is duck!")


duck = Duck("Steve")
duck.fly()
duck.paws()

print(issubclass(Cat, Animals))
print(issubclass(Dog, Animals))
print(issubclass(Animals, Dog))

print(isinstance(dog, Animals))


class Human:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating! He is a human!")

    def sleep(self):
        print(f"{self.name} is sleeping! He is a human!")

    def study(self):
        print(f"{self.name} is studying. He is a human!")

    def work(self):
        print(f"{self.name} is studying. He is a human!")


class Centaur(Animals, Human):
    def count_hands(self):
        print(f"{self.name} has two hands!")


centaur = Centaur("Arnold")
centaur.eat()
centaur.sleep()
centaur.study()
centaur.work()
