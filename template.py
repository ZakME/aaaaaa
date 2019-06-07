# Text Based RPG

class player(object):
    def __init__(self, name, origin, age):
        self.pName = name
        self.pOrigin = origin
        self.pAge = age
        self.health = 10
        self.damage = 5
    
    def attack(self, monster):
        print("You have challenged " + monster.mName + " of " + monster.mOrigin + " to a battle!")
        print("You: " + str(self.health) + " HP")
        print(monster.mName + ": " + str(monster.mHealth) + " HP")
        print("You slice " + monster.mName + " with your sword dealing 5 damage!")
        monster.mHealth = monster.mHealth - self.damage
        if monster.mHealth < 0:
            monster.mHealth = 0
        print(monster.mName + " has fallen to " + str(monster.mHealth) + " health.")

class monsters(object):
    def __init__(self, name, origin, health):
        self.mName = name
        self.mOrigin = origin
        self.mHealth = health

class gamemap(object):
    def __init__(self, plyr):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.player = plyr
        self.monsterz = [monsters("Hayneous Hay", "Colarado", 1)]
        self.location = (str(plyr.pOrigin) + "ia")
        self.rooms = [["In " + self.location + ", you, " + str(plyr.pName) + """, lay fast asleep in your bed. A sudden surge of energy 
        pulses through your body and you open your eyes to find that you have been sent to a small room.
        A sword lies to your left and you pick it up. A wooden door lies ahead, will you proceed?""", 1, 0], ["""
        The room you have entered is dark, lit by one torch on the left stone brick wall. A small stash of hay 
        begins to move in the back right corner of the room. It is a hay creature! It seems to be very weak,
        but you still approach with caution. The hay creature's movements reveal a door, but it won't let you through.""", 5, 1, self.monsterz[0]]]
        self.currentRoom = self.rooms[0]
        self.choice = 0
    
    def initMonsters(self):
        self.monsterz.append(monsters("Bob", "Bobia", 10))

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
            self.defaultChoice()
        elif self.currentRoom[1] == 5:
            self.defaultChoice()
            
    
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
            print(str(self.currentRoom[1]))
            if self.currentRoom[1] != 1 and self.currentRoom[1] != 5 and self.currentRoom[1] != 9:
                self.typeTwoSixTen()
            else:
                self.updateRoom(1)
                self.printSquiggle()
                print("You decide to proceed into the next territory.")
                self.describeRoom()
                self.printSquiggle()
                self.options()

    def invalid(self, choice):
        if (choice.lower()) != "rest" and (choice.lower()) != "status" and (choice.lower()) != "proceed" and (choice.lower()) != "attack":
            print("Invalid Option.")
            self.options()

    def updateRoom(self, room):
        self.currentRoom = self.rooms[room]

    def printrooms(self):
        print(self.rooms[0][0])
    
    def describeRoom(self):
        print(self.currentRoom[0])
        self.options()
    
    def attack(self, choice, monsterNum):
        global p1
        if (choice.lower()) == "attack":
            p1.attack(monsterNum)
    
    def printSquiggle(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def defaultChoice(self):
        if self.currentRoom[2] == 1:
            self.choice = str(input("What will you do? Rest, Status, or Attack? "))
            if (self.choice.lower()) == "proceed":
                print("Invalid Option.")
                self.defaultChoice()
            self.attack(self.choice, self.currentRoom[3])
        else:
            self.choice = str(input("What will you do? Rest, Status, or Proceed? "))
        self.invalid(self.choice)
        self.rest(self.choice)
        self.status(self.choice)
        self.proceed(self.choice)
        

    def typeTwoSixTen(self):
        if self.choice == "proceed":
                self.choice = input("Which door would you like to travel through (1 or 2)? ")
                if self.choice == str(1):
                    self.updateRoom(3)
                elif self.choice == str(2):
                    self.updateRoom(2)
                else:
                    print("Invalid option.")
                    self.defaultChoice()

def main():
    global p1
    p1 = player("Bob", "Human", "10")
    game = gamemap(p1)
    game.initMonsters()
    game.describeRoom()
    

main()
    

