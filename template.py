# Text Based RPG

class player(object):
    def __init__(self, name, origin, age):
        self.pName = name
        self.pOrigin = origin
        self.pAge = age

class gamemap(object):
    def __init__(self, plyr):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.player = plyr
        self.location = (str(plyr.pOrigin) + "ia")
        self.rooms = [["In " + self.location + ", you, " + str(plyr.pName) + """, lay fast asleep in your bed. A sudden surge of energy 
        pulses through your body and you open your eyes to find that you have been sent to a small room.
        A sword lies to your left and you pick it up. A wooden door lies ahead, will you proceed?""", 1], ["""
        The room you have entered is dark, lit by one torch on the left stone brick wall. A small stash of hay 
        begins to move in the back right corner of the room. It is a hay monster! It seems to be very weak,
        but you still exercise caution. The hay monster blocks reveals a door, but won't let you through.""", 5]]
        self.currentRoom = self.rooms[0]
        self.choice = 0

    def options(self):
        #Type 1 = Proceed 1 door, rest, status
        #Type 2 = Proceed 2 doors, rest, status
        #Type 3 = Proceed 3 doors, rest, status
        #Type 4 = Proceed 4 doors, rest, status
        #Type 5 = Type 1 + Enemy - rest
        #Type 6 = Type 2 + Enemy - rest
        #Type 7 = Type 3 + Enemy - rest
        #Type 8 = Type 4 + Enemy - rest
        #Type 9 = Type 1 + item OR type 5 + item
        #Type 10 = Type 2 + item OR type 6 + item
        #Type 11 = Type 3 + item OR type 7 + item
        #Type 12 = Type 4 + item OR type 8 + item

        if self.currentRoom[1] == 1:
            self.choice = str(input("What will you do? Rest, Status, or Proceed? "))
            self.invalid(self.choice)
            self.rest(self.choice)
            self.status(self.choice)
    
    def rest(self, choice):
        if (choice.lower()) == "rest":
            print("Resting.")
            self.options()

    def status(self, choice):
        if (choice.lower()) == "status":
            print("You are feeling healthy and are carrying your sword in hand.")
            self.options()

    def proceed(self, choice):
        if (choice.lower()) == "proceed":
            self.updateRoom(1)
            print("You decide to proceed into the next territory.")

    def invalid(self, choice):
        if (choice.lower()) != "rest" and (choice.lower()) != "status" and (choice.lower()) != "proceed":
            print("Invalid Option.")
            self.options()

    def updateRoom(self, room):
        self.currentRoom = self.rooms[room]

    def printrooms(self):
        print(self.rooms[0][0])

def main():
    p1 = player("Bob", "Human", "10")
    game = gamemap(p1)
    def describeRoom():
        print(game.currentRoom[0])
        game.options()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

main()
    

