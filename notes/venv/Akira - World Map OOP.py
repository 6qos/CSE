Rooms= {
    'CLUB_ROOM': {
        'NAME': "The Club Room",
        'DESCRIPTION': "This is the room that you are in.",
        'PATHS': {
            'NORTH': "OUTSIDE_OF_CLUB_ROOM"

        }
    },
    'OUTSIDE_OF_CLUB_ROOM': {
        'NAME': "Outside of the Club Room",
        'DESCRIPTION': "You are now Outside.",
        'PATHS': {
            'EAST': "TENNIS_COURT",
            'WEST': "GYM",
            'SOUTH': "CLUB_ROOM",
            'NORTH': "SCHOOL_YARD"
        }
    },
    'TENNIS_COURT': {
        'NAME': "Tennis Court",
        'DESCRIPTION': "You can play Tennis here.",
        'PATHS': {
            'WEST': "OUTSIDE_OF_CLUB_ROOM"

        }
    },
    'GYM': {
        'NAME': "Gymnasium",
        'DESCRIPTION': "This is where you play sports.",
        'PATHS': {
            'EAST': "OUTSIDE_OF_CLUB_ROOM"

        }
    },
    'SCHOOL_YARD': {
        'NAME': "School Yard",
        'DESCRIPTION': "This is the school yard.",
        'PATHS': {
            'SOUTH': "OUTSIDE_OF_CLUB_ROOM",
            'NORTH': "SCHOOL",
            'WEST': "POOL",
            'EAST': "STEEP_HILL"
        }
    },
    'SCHOOL': {
        'NAME': "Inside the School.",
        'DESCRIPTION': "You are in the school.",
        'PATHS': {
            'SOUTH': "SCHOOL_YARD",
            'UP': "SCHOOL_FLOOR_2",
            'NORTH': "BOYS_BATHROOM",
            'EAST': "GIRLS_BATHROOM",
            'WEST': "FIELD",
            'DOWN': "UNDER_THE_SCHOOL"
        }
    },
    'SCHOOL_FLOOR_2': {
        'NAME': "Floor 2",
        'DESCRIPTION': "This is the second floor.",
        'PATHS': {
            'DOWN': "SCHOOL",
            'NORTH': "CLASS_ROOM_1"
        }
    },
    'CLASS_ROOM_1': {
        'NAME': "Classroom",
        'DESCRIPTION': "A random classroom.",
        'PATHS': {
            'SOUTH': "SCHOOL_FLOOR_2"
        }
    },
    'POOL': {
        'NAME': "The Pool.",
        'DESCRIPTION': "A place where you swim.",
        'PATHS': {
            'EAST': "SCHOOL_YARD",
            'DOWN': "IN_THE_POOL"
        }
    },
    'BOYS_BATHROOM': {
        'NAME': "Boys Bathroom",
        'DESCRIPTION': "The Bathroom",
        'PATHS': {
            'SOUTH': "SCHOOL"
        }
    },
    'GIRLS_BATHROOM': {
        'NAME': "Girls Bathroom",
        'DESCRIPTION': "THe Bathroom",
        'PATHS': {
            'WEST': "SCHOOL"
        }
    },
    'FIELD': {
        'NAME': "Field",
        'DESCRIPTION': "It's THe Field",
        'PATHS': {
            'EAST': "SCHOOL"
        }
    },
    'IN_THE_POOL': {
        'NAME': "You are swimming in the pool",
        'DESCRIPTION': "You are in the pool",
        'PATHS': {
            'UP': "POOL"
        }
    },
    'UNDER_THE_SCHOOL': {
        'NAME': "Under the School",
        'DESCRIPTION': "you are under the school",
        'PATHS': {
            'UP': "SCHOOL"
        }
    },
    'STEEP_HILL': {
        'NAME': "A steep hill",
        'DESCRIPTION': "A Steep Hill",
        'PATHS': {
            'WEST': "SCHOOL_YARD"
        }
    },
}

# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["CLUB_ROOM"]  # This is your current location
playing = True

# Controller
while playing:
    print(current_node['NAME'])

    command = input("<_")
    if command.lower() in ['q', 'quit', 'exit', 'Q', 'Quit', 'Exit', 'E']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized")

        
        
        
        