class Laptop(object):
    def __init__(self, screen_resolution, extra_space=1000, colour="Cobalt"):
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = colour
        self.os = "Linux"
        self.functioning = True

    def charge(self, time):
        if self.functioning:
            if self.charge >= 100:
                print("The Computer is already Charged.")
                return
            self.battery_left += time
            if self.battery_left > 100:
                print("The Computer quickly charges.")
            else:
                print("The computer is now at %d%%" % self.battery_left)


        else:
            print("It's Broken. Good Job.")

def smash(self):
    self.functioning = False
    print("I took the laptop...")
    print()
    print()
    print()
    print("...AND I THREW IT ON THE GROUND!!!!")


my_computer = Laptop("1920x1080", 10000, "Black")
your_computer = Laptop("10x10", 0, "Orange")
wiebe_computer = Laptop("9000000000000x900000000000000", 999999999999999999, "Awesome")
default_computer = Laptop("1920x1080")


def use(self, time):
    self.battery_left -= time
    print("You use the laptop for %s minutes" % time)

print(Laptop)