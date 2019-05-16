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

# Option 2 - Use Strings, but more difficult controller
R19A = Room("Mr. Wiebe's Room", "parking_lot")
parking_lot = Room("The Parking Lot", None, "R19A")
Black_top = Room("The Black Top", None, "Blacktop")
Gym = Room("The Gym", None, "Gym")
Cafeteria = Room("The Cafeteria",None, "Cafeteria")
Field = Room("The Field", None, "Field")

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


