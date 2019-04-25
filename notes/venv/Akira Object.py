class Mclaren(object):
    def __init__(self, gas_capacity=100, battery=100, colour="Black"):
        self.gas_capacity = gas_capacity
        self.color = colour
        self.mph = 300
        self.battery = battery
        self.driving = True

    def charge(self, time):
        if self.driving:
            if self.gas_capacity >= 100:
                print("The gas tank is already full.")
                return
            self.gas_capacity += time
            if self.gas_capacity > 100:
                print("You are putting in gas.")
            else:
                print("The car has %d gas left" % self.gas_capacity)
        else:
            print("THe gas is overspilling.")

    def crash(self):
        self.driving = False
        print("You were not paying attention...")
        print()
        print()
        print()
        print("...AND YOU CRASHED INTO A TREE!!!!")


my_Mclaren = Mclaren(10000, 100, "Black")
your_Mclaren = Mclaren(10,100, "Orange")
akira_Mclaren = Mclaren(1000000, 999999999999999999, "Crimson")
default_Mclaren = Mclaren(100, 100, "White")


def use(self, time):
    self.gas_capacity -= time
    print("You drive the car for %s minutes" % time)
