class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None, west=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = "ENTER DESCRIPTION HERE"


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """

        :param new_location:
        """
        self.current_location = new_location

    def find_room(self, direction):
        """

        :param direction: A string (all lowercase), with a cardinal direction
        :return: a room object if it exist, None if it does not
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]

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
    def __init__(self, name, armour_amt, armour_type):
        super(Armour, self).__init__(name)
        self.armour_amt = armour_amt
        self.armour_type = armour_type


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
    def __init__(self, name, health, weapon, armour, armour_type):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armour = armour
        self.armour_type = armour_type

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
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


sword = Sword("Sword", 10)
canoe = Sword("Canoe", 84)
wiebe_armour = Armour("Armour of the Gods", "Gods Armour", 10000000000000000)


rc = Character("orc", 100, Sword(sword), Armour, "Generic Armour")
weibe = Character("weibe", 10000000, Sword(sword), Armour, "God Armour")

orc.attack(weibe)
weibe.attack(orc)

class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None, description="INSERT DESCRIPTION HERE"):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """This method moves a player to a new location
        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction, and finds the variable of the
        room.
        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]



# These are the instances of the rooms (Instantiation)

# Option 1 - Use the Variables, but fix later
R19A = Room("Mr. Wiebe's Room")
parking_lot = Room("The Parking Lot", None, R19A)

R19A.north = parking_lot

# Option 2 - Use Strings, but more difficult controller
R19A = Room("Mr. Wiebe's Room", "parking_lot")
parking_lot = Room("The Parking Lot", None, "R19A")

player = Player(R19A)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True


# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input("<_")
    if command.lower() in ['q', 'quit', 'exit', 'Q', 'Quit', 'Exit', 'E']:
        playing = False
    elif command in direction:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized")

        player = Player("CLUB_ROOM")
        direction = ['north', 'south', 'east', 'west', 'up', 'down']
        playing = True


