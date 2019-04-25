class Items(object):
    def __init__(self, name):
        self.name = name


class Sword(Items):
    def __init__(self, name, damage):
        super(Sword, self).__init__(name)
        self.damage = damage


class Shirts(Items):
    def __init__(self):
        super(Shirts, self).__init__("Shirts")


class Pants(Items):
    def __init__(self):
        super(Pants, self).__init__("Pants")


class Shorts(Items):
    def __init__(self):
        super(Shorts, self).__init__("Shorts")


class Armour(Items):
    def __init__(self, name, armour_amt):
        super(Armour, self).__init__(name)
        self.armour_amt = armour_amt


class Furniture(Items):
    def __init__(self):
        super(Furniture, self).__init__("Furniture")


class Cellphone(Items):
    def __init__(self):
        super(Cellphone, self).__init__("Cellphone")


class SportsBall(Items):
    def __init__(self):
        super(SportsBall, self).__init__("SportsBall")


class FootWear(Items):
    def __init__(self):
        super(FootWear, self).__init__("Footwear")


class Food(Items):
    def __init__(self):
        super(Food, self).__init__("Food")


class Drinks(Items):
    def __init__(self):
        super(Drinks, self).__init__("Drinks")


class MagicSlip(Items):
    def __init__(self):
        super(MagicSlip, self).__init__("MagicSlip")


class Candy(Items):
    def __init__(self):
        super(Candy, self).__init__("Candy")


class Shield(Items):
    def __init__(self):
        super(Shield, self).__init__("Shield")


class Book(Items):
    def __init__(self):
        super(Book, self).__init__("Book")


class Character(object):
    def __init__(self, name, health, weapon, armour):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armour = armour

    def take_damage(self, damage):
        if damage < self.armour.armour_amt:
            print("No Damage is done because of your armour!")
        else:
            self.health -= damage - self.armour.armour_amt
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
            print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks for %d damage" % (self.name)(target.name)(self.weapon.damage))
        target.take_damage(self.weapon.damage)


sword = Sword("Sword", 10)
canoe = Sword("Canoe", 84)
wiebe_armour = Armour("Armour of the Gods", 10000000000000000)


orc = Character("orc", 100, Sword, Armour, ("Generic Armour"))
weibe = Character("weibe", 10000000, Sword, Armour, ("Gods Armour"), 4)

orc.attack(weibe)
weibe.attack(orc)
orc.attack(weibe)
weibe.attack(orc)
weibe.attack(orc)
