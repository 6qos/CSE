class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None, west=None, up=None, down=None, description="INSERT DESCRIPTION HERE"):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
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
R19A = Room("Mr. Wiebe's Room", 'parking_lot', None, None, None, None, None, "R19A")
parking_lot = Room("The Parking Lot", 'Black_top', 'R19A', None, None, None, None, "Parking Lot")
Black_top = Room("The Black Top", 'Gym', 'parking_lot', None, None, None, None, "Black Top")
Gym = Room("The Gym", 'Cafeteria', "Black_top", None, None, None, None, "Gym")
Cafeteria = Room("The Cafeteria", 'Field', 'Gym', None, None, None, None, "Cafeteria")
Field = Room("The Field", 'Pool', 'Cafeteria', None, None, None, None, "Field")
Pool = Room("The Pool", 'Auditorium', "Pool", None, None, None, None, "Pool")
Auditorium =("The Auditorium", 'Boys_Locker_Room', 'Pool', None, None, None, None, "Auditorium")
Boys_Locker_Room = Room("Boys Locker Room", 'Weight_Room', 'Auditorium', None, None, None, None, "Locker Room")
Girls_Locker_Room = Room("Girls Lcoker Room", 'Pool', None, None, None, None, "Girls Locker Room")
Computer_Lab = Room("The Computer Lab", 'Science_Lab', 'Field', None, None, None, None, "Computer Lab")
Science_Lab = Room("The Science Room",'Bathrooms', 'Computer_Lab', None, None, None, None,  "Science Lab")
Bathrooms = Room("The Bathroom", 'Boys_Locker_Room', 'Girls_locker_Room', None, None, None, None, "Bathroom")
Weight_Room = Room("The Weight Room", 'Bathrooms', 'Boys_Locker_Room', None, None, None, None, "Weight Room")
Storage_Room = Room("Storage Room", 'English_Classroom', 'Weight_Room', None, None, None, None, "Storage Room")
English_Classroom = Room("English Classroom", None, 'Storage_Room', None, None, None, None, "English Classroom")
Mathematics = Room("Math_Class", None, 'Emglish_Classroom', None, None, None, None, "Mathematics")
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
    elif command in directions:
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


