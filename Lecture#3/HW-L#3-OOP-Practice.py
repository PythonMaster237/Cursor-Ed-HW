import random


class Person:
    def __init__(self, name, age, money, own_home):
        self.name = name
        self.age = age
        self.money = money
        self.own_home = own_home

    def print_information(self):
        print(f"Name: {self.name} \nAge: {self.age} \nMoney: {self.money} \nOwn home: {self.own_home}")

    def make_money(self, money):
        self.money += money

    def buy_house(self, value):
        if value.cost > self.money:
            print("You can`t buy this house.")
        else:
            print("You can buy this house.")


class House:
    houses_list = []

    def __init__(self, area, cost):
        self.area = area
        self.cost = cost
        self.houses_list.append(self)

    def apply_discount(self, percent):
        self.cost = self.cost*(1-(percent/100))


class Realtor:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Realtor, cls).__new__(cls)
        return cls.instance

    def __init__(self, name, discount, person, houses=House.houses_list):
        self.name = name
        self.discount = discount
        self.houses = houses
        self.person = person

    def print_houses_info(self):
        if self.houses == []:
            print("There is no houses.")
        else:
            for i in House.houses_list:
                print(f"There is a house with a required area of {i.area}m2. Cost = {i.cost}")

    def steal_money(self):
        if random.randint(1, 10) == 1:
            self.person.money = 0
            print("Realtor stole your money.")
        else:
            print("Your money in your pocket.")

    def after_discount(self, num_of_house):
        house = self.houses[num_of_house-1]
        house.cost = house.cost*(1-(self.discount/100))


house_1 = House(45, 30000)
house_2 = House(90, 70000)
house_3 = House(30, 15000)

person_1 = Person("Arnold", 26, 29000, 'No')

realtor = Realtor('John', 20, person_1)

person_1.buy_house(house_1)
realtor.print_houses_info()
realtor.after_discount(1)
print("Print after discount")
realtor.print_houses_info()
person_1.buy_house(house_1)
