# Names: John Coughlin, Seth Flowers

# Final Pi Project

# Description:


from tkinter import *
import RPi.GPIO as GPIO
from time import time

class GUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg = "white")
        self.master = master
        self.setupGUI()
        self.DescriptionText = ""
        self.ChoicesText = ""
        self.ButtonText = ["", "", "", "", ""]
        self.ButtonCommand = [[None], [None], [None], [None], [None]]

    def setupGUI(self):
        self.Picture = Label(self.master, text = "Picture", bg = "grey", width = 24, height = 6)
        self.Picture.grid(row=0, column=0, rowspan=6, columnspan=6, sticky=N+S+E+W)

        self.Space1 = Label(self.master, text = "", width = 2, height = 2)
        self.Space1.grid(row=1, column=6, rowspan = 2, sticky=N+S+E+W)

        self.Space2 = Label(self.master, text = "", width = 2, height = 1)
        self.Space2.grid(row=4, column=6, sticky=N+S+E+W)

        self.Space3 = Label(self.master, text = "", width = 2, height = 1)
        self.Space3.grid(row=6, column=6, sticky=N+S+E+W)

        self.Space4 = Label(self.master, text = "", width = 2, height = 1)
        self.Space4.grid(row=8, column=6, sticky=N+S+E+W)

        self.Space5 = Label(self.master, text = "", width = 2, height = 1)
        self.Space5.grid(row=10, column=6, sticky=N+S+E+W)

        self.TextDescription = Label(self.master, text = "Location Description.", anchor = W, width = 24, height = 5)
        self.TextDescription.grid(row=7, column=0, rowspan=5, columnspan=6, sticky=W)

        self.TextChoices = Label(self.master, text = "Choices", anchor = W, bg = "grey", width = 24, height = 1)
        self.TextChoices.grid(row=0, column=7, columnspan=6, sticky=N+S+E+W)

        self.Button = [None, None, None, None, None]
        self.Button[0] = Button(self.master, bg = "grey", text="Button0", anchor = W, command = lambda:self.process(0), width = 24, height = 1)
        self.Button[0].grid(row=3, column=7, columnspan=6, sticky=N+S+E+W)

        self.Button[1] = Button(self.master, bg = "grey", text="Button1", anchor = W, command = lambda:self.process(1), width = 24, height = 1)
        self.Button[1].grid(row=5, column=7, columnspan=6, sticky=N+S+E+W)

        self.Button[2] = Button(self.master, bg = "grey", text="Button2", anchor = W, command = lambda:self.process(2), width = 24, height = 1)
        self.Button[2].grid(row=7, column=7, columnspan=6, sticky=N+S+E+W)

        self.Button[3] = Button(self.master, bg = "grey", text="Button3", anchor = W, command = lambda:self.process(3), width = 24, height = 1)
        self.Button[3].grid(row=9, column=7, columnspan=6, sticky=N+S+E+W)

        self.Button[4] = Button(self.master, bg = "grey", text="Button4", anchor = W, command = lambda:self.process(4), width = 24, height = 1)
        self.Button[4].grid(row=11, column=7, columnspan=6, sticky=N+S+E+W)

    def setDescription(self, text):
        self.DescriptionText = text
        self.TextDescription["text"] = text

    def setChoices(self, text):
        self.ChoicesText = text
        self.TextChoices["text"] = text

    def setButton(self, buttonNumber, text):
        self.ButtonText[buttonNumber] = text
        self.Button[buttonNumber]["text"] = text

    def setButtonCommand(self, buttonNumber, command):
        self.ButtonCommand[buttonNumber] = command

    def process(self, buttonNumber):
        global currentScreen
        global flags
        global CurrentTime
        CurrentTime = time()
        if(CurrentTime-Start > Stop):
            TimesUp()
        if(self.ButtonCommand[buttonNumber][0] == None):
            pass
        #"go", area
        elif(self.ButtonCommand[buttonNumber][0] == "go"):
            currentScreen = self.ButtonCommand[buttonNumber][1]
            self.update()
        #"event", event
        elif(self.ButtonCommand[buttonNumber][0] == "event"):
            if(str(currentScreen) == "Event"):
                self.ButtonCommand[buttonNumber][1].Area = currentScreen.Area
                currentScreen = self.ButtonCommand[buttonNumber][1]
                self.update()
            else:
                self.ButtonCommand[buttonNumber][1].Area = currentScreen
                currentScreen = self.ButtonCommand[buttonNumber][1]
                self.update()
        #"give flag", area/event, flag, (flag value/clear)
        elif(self.ButtonCommand[buttonNumber][0] == "give flag"):
            if(str(currentScreen) == "Event"):
                if(str(self.ButtonCommand[buttonNumber][1]) == "Event"):
                    if(self.ButtonCommand[buttonNumber][3] == "clear"):
                        flags[self.ButtonCommand[buttonNumber][2]] = []
                        self.ButtonCommand[buttonNumber][1].Area = currentScreen.Area
                        currentScreen = self.ButtonCommand[buttonNumber][1]
                        self.update()
                    else:
                        flags[self.ButtonCommand[buttonNumber][2]].append(self.ButtonCommand[buttonNumber][3])
                        self.ButtonCommand[buttonNumber][1].Area = currentScreen.Area
                        currentScreen = self.ButtonCommand[buttonNumber][1]
                        self.update()
                else:
                    if(self.ButtonCommand[buttonNumber][3] == "clear"):
                        flags[self.ButtonCommand[buttonNumber][2]] = []
                        currentScreen = self.ButtonCommand[buttonNumber][1]
                        self.update()
                    else:
                        flags[self.ButtonCommand[buttonNumber][2]].append(self.ButtonCommand[buttonNumber][3])
                        currentScreen = self.ButtonCommand[buttonNumber][1]
                        self.update()
            else:
                if(str(self.ButtonCommand[buttonNumber][1]) == "Event"):
                    if(self.ButtonCommand[buttonNumber][3] == "clear"):
                        flags[self.ButtonCommand[buttonNumber][2]] = []
                        self.ButtonCommand[buttonNumber][1].Area = currentScreen
                        currentScreen = self.ButtonCommand[buttonNumber][1]
                        self.update()
                    else:
                        flags[self.ButtonCommand[buttonNumber][2]].append(self.ButtonCommand[buttonNumber][3])
                        self.ButtonCommand[buttonNumber][1].Area = currentScreen
                        currentScreen = self.ButtonCommand[buttonNumber][1]
                        self.update()
                else:
                    if(self.ButtonCommand[buttonNumber][3] == "clear"):
                        flags[self.ButtonCommand[buttonNumber][2]] = []
                        currentScreen = self.ButtonCommand[buttonNumber][1]
                        self.update()
                    else:
                        flags[self.ButtonCommand[buttonNumber][2]].append(self.ButtonCommand[buttonNumber][3])
                        currentScreen = self.ButtonCommand[buttonNumber][1]
                        self.update()
        #"event flag", flag, pass condition, passevent, failevent
        elif(self.ButtonCommand[buttonNumber][0] == "event flag"):
            if(str(currentScreen) == "Event"):
                if(flags[self.ButtonCommand[buttonNumber][1]] == self.ButtonCommand[buttonNumber][2]):
                    self.ButtonCommand[buttonNumber][3].Area = currentScreen.Area
                    currentScreen = self.ButtonCommand[buttonNumber][3]
                    self.update()
                else:
                    self.ButtonCommand[buttonNumber][4].Area = currentScreen.Area
                    currentScreen = self.ButtonCommand[buttonNumber][4]
                    self.update()
            else:
                if(flags[self.ButtonCommand[buttonNumber][1]] == self.ButtonCommand[buttonNumber][2]):
                    self.ButtonCommand[buttonNumber][3].Area = currentScreen
                    currentScreen = self.ButtonCommand[buttonNumber][3]
                    self.update()
                else:
                    self.ButtonCommand[buttonNumber][4].Area = currentScreen
                    currentScreen = self.ButtonCommand[buttonNumber][4]
                    self.update()
        elif(self.ButtonCommand[buttonNumber][0] == "function"):
            self.ButtonCommand[buttonNumber][1]()
        elif(self.ButtonCommand[buttonNumber][0] == "return" and str(currentScreen) == "Event"):
            currentScreen = currentScreen.Area
            self.update()
            

    def update(self):
        self.setDescription(currentScreen.DescriptionText)
        self.setChoices(currentScreen.ChoicesText)
        self.setButton(0, currentScreen.ButtonText[0])
        self.setButton(1, currentScreen.ButtonText[1])
        self.setButton(2, currentScreen.ButtonText[2])
        self.setButton(3, currentScreen.ButtonText[3])
        self.setButton(4, currentScreen.ButtonText[4])
        self.setButtonCommand(0, currentScreen.ButtonCommand[0])
        self.setButtonCommand(1, currentScreen.ButtonCommand[1])
        self.setButtonCommand(2, currentScreen.ButtonCommand[2])
        self.setButtonCommand(3, currentScreen.ButtonCommand[3])
        self.setButtonCommand(4, currentScreen.ButtonCommand[4])
            
class Screen:
    def __init__(self):
        self.DescriptionText = ""
        self.ChoicesText = ""
        self.ButtonText = ["", "", "", "", ""]
        self.ButtonCommand = [[None], [None], [None], [None], [None]]

    def setText(self, text):
        self.DescriptionText = text[0]
        self.ChoicesText = text[1]
        self.ButtonText = text[2:len(text)]

    def setCommand(self, command):
        self.ButtonCommand = command

class Area(Screen):
    def __init__(self):
        Screen.__init__(self)

    def __str__(self):
        return "Area"

class Event(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.Area = None

    def __str__(self):
        return "Event"
        
# Setup method

def Setup():
    #Tkinter:
    
    window = Tk()
    window.title("Escape From The Facility")
    GameWindow = GUI(window)
    
    #Creating all the story areas:
    
    Start = Area()
    Area1 = Area()
    Area2 = Area()
    Area3 = Area()
    Area4 = Area()
    Area5 = Area()
    Area6 = Area()
    Area7 = Area()
    Area8 = Area()
    Area9 = Area()
    Area10 = Area()
    Area11 = Area()
    Area12 = Area()
    Area13 = Area()

    #setting the text in all the story areas:

    Start.setText(["You're in a small room with garbage strewn about the place", "What do you do?", "Look around", "Leave the room", "", "", ""])
    Area1.setText(["You're in a empty hallway.", "What do you do?", "Look around", "Leave the area", "", "", ""])
    Area2.setText(["You're in a empty hallway.  The door to your right is ajar.", "What do you do?", "Look around", "Leave the area", "", "", ""])
    Area3.setText(["You find yourself in what looks like a medium sized storage room", "What do you do?", "Look around", "Leave the area", "", "", ""])
    Area4.setText(["You enter into an empty hallway.  You see two doors to the left and right in the back.", "What do you do?", "Look around", "Leave the area", "", "", ""])
    Area5.setText(["You're in a small room with a table in the middle with some chairs.", "What do you do?", "Look around", "Leave the area", "", "", ""])
    Area6.setText(["You're in a small room.  You smell something.", "Area 6 choices:", "Look around", "Leave the area", "", "", ""])
    Area7.setText(["You're in a small empty room.", "What do you do?", "Look around", "Leave the area", "", "", ""])
    Area8.setText(["You're in a small empty room.", "What do you do?", "Look around", "Leave the area", "", "", ""])
    Area9.setText(["You find yourself in a small corridor.", "What do you do?", "Look around", "Leave the area", "", "", ""])
    Area10.setText(["You find yourself in another office.", "What do you do?", "Look around", "Leave the area", "", "", ""])
    Area11.setText(["You find yourself in what looks like a office with a door on each side.", "What do you do?", "Look around", "Leave the area", "", "", ""])
    Area12.setText(["You find yourself in another office.", "What do you do?", "Look around", "Leave the area", "", "", ""])
    Area13.setText(["You see a big bomb in the middle of the room.", "What do you do?", "Defuse bomb", "", "", "", ""])

    #Creating all flags:

    global flags
    flags["ID card"] = []
    flags["Card readers"] = []
    flags["Fingerprint"] = []
    flags["Computers"] = []
    flags["Bomb"] = []

    #Creating all the events:
    
    StartEvent = Event()
    StartLook = Event()
    StartLeave = Event()

    Area1Look = Event()
    Area1Leave = Event()

    Area2Look = Event()
    Area2Leave = Event()

    Area3Look = Event()
    Area3Leave = Event()

    Area4Look = Event()
    Area4Leave = Event()

    Area5Look = Event()
    Area5Leave = Event()
    IDCardFound = Event()
    
    Area6Look = Event()
    Area6Leave = Event()
    GuardFound = Event()
    GuardTaken = Event()
    
    Area7Look = Event()
    Area7Leave = Event()
    Puzzle1 = Event()
    Puzzle1Pass = Event()
    Puzzle1Fail = Event()

    Area8Look = Event()
    Area8Leave = Event()
    Puzzle2Pass = Event()
    Puzzle2Fail = Event()

    Area9Look = Event()
    Area9Leave = Event()

    Area10Look = Event()
    Area10Leave = Event()
    FinalPuzzle1 = Event()
    FinalPuzzle1Pass = Event()

    Area11Look = Event()
    Area11Leave = Event()
    FinalPuzzle2 = Event()
    FinalPuzzle2Pass = Event()

    Area12Look = Event()
    Area12Leave = Event()
    FinalPuzzle3 = Event()
    FinalPuzzle3Pass = Event()

    Area13Bomb

    global GoodEnd
    global BadEnd
    GoodEnd = Event()
    BadEnd = Event()

    #setting the text in all the events:

    StartEvent.setText(["You find yourself loosely tied up in a small room.", "What do you do?", "Free yourself", "", "", "", ""])
    StartLook.setText(["Looking around the room, you don't see much of interest", "You find:", "Used wrappers", "Crumpled papers", "", "", "Go back"])
    StartLeave.setText(["The room your in has three exits.  One to your left, another in front of you, and finally one to your right", "What do you do?", "Go through the left door", "Go through the middle door", "Go through the right door", "", "Go back"])

    Area1Look.setText(["You don't see anything of interest around here besides small windows to your left.", "You find:", "", "", "", "", "Go back"])
    Area1Leave.setText(["The hallway you're in only has two exits.  The way you came in and the door at the end of the hallway.", "You can leave through:", "The door you came from", "The door in the back", "", "", "Go back"])

    Area2Look.setText(["Looking around the hallway, you see nothing of interest.", "You find:", "", "", "", "", "Go back"])
    Area2Leave.setText(["The hallway you're in has three exits.  The door behind you, the door to your right, and the door in front of you", "You can leave through:", "The door behind you", "The door to your right", "The door in front of you", "", "Go back"])

    Area3Look.setText(["Looking around the storage area you find a disorganized mess.  It's like whoever was using it was in a rush to get whatever was neccessary out before leaving.", "You find:", "Locked storage lockers", "A mostly empty backpack", "A broken cellphone", "Some papers on the ground", "Go back"])
    Area3Leave.setText(["The storage area has two exits.  One door leads to a hallway, the other leads to the room you woke up in.", "Where do you want to go?", "The room you woke up in", "The hallway", "", "", "Go back"])

    Area4Look.setText(["You see that the hallway is completely empty.", "You find:", "", "", "", "", "Go back"])
    Area4Leave.setText(["You find out that the doors behind you are locked, so you can only choose from the two doors in front of you.", "You can leave through:", "The door on the left", " The door on the right", "", "", "Go back"])

    Area5Look.setText(["Looking around the small room you find something on the ground", "You find:", "an ID card", "", "", "", "Go back"])
    Area5Leave.setText(["There is only one door that isn't locked.", "What do you do?", "Go through that door", "", "", "", "Go back"])
    IDCardFound.setText(["You've picked up the ID card.", "...", "Okay", "", "", "", ""])
    
    Area6Look.setText(["Looking around the room you find the body of what looks like a guard.", "You find:", "Dead guard", "", "", "", "Go back"])
    Area6Leave.setText(["You can only go through one door.", "You can leave through:", "That door", "", "", "", "Go back"])
    GuardFound.setText(["You've found a body of a dead guard.", "What do you do?", "Take it with you", "", "", "", "Go back"])
    GuardTaken.setText(["You've decided to take the body with you.", "...", "Okay", "", "", "", ""])
    
    Area7Look.setText(["Looking around the small empty room.", "You find:", "4 card readers next to the door in the back", "", "", "", "Go back"])
    Area7Leave.setText(["You find two doors in the room.", "You can leave through:", "The door behind you.", "The door in the back", "", "", "Go back"])
    Puzzle1.setText(["You come up to the card readers", "Slide the card through the", "1st card reader", "2nd card reader", "3rd card reader", "4th card reader", "done"])
    Puzzle1Pass.setText(["The door unlocks and you are let through.", "...", "Okay", "", "", "", ""])
    Puzzle1Fail.setText(["The door remains locked so you can't proceed.", "...", "Okay", "", "", "", ""])

    Area8Look.setText(["Looking around the small empty room, you see at the other door you see a fingerprint scanner on it.", "You find:", "", "", "", "", "Go back"])
    Area8Leave.setText(["In the room there are two doors.  The one you came through, and the one with the fingerprint scanner.", "You can leave through:", "The door you came from", "The door with the scanner", "", "", "Go back"])
    Puzzle2Pass.setText(["Using the dead guard's fingerprint, you are let through.", "...", "Okay", "", "", "", ""])
    Puzzle2Fail.setText(["You try using your own fingerprint, but it fails.", "...", "Okay", "", "", "", ""])

    Area9Look.setText(["Looking around the corridor, you find nothing of interest.", "You find:", "", "", "", "", "Go back"])
    Area9Leave.setText(["You find your only able to go through one door", "You can leave through:", "Go through that door", "", "", "", "Go back"])

    Area10Look.setText(["Looking around the office you find a desk with a laptop on it.", "You find:", "Laptop", "", "", "", "Go back"])
    Area10Leave.setText(["There is only one door you can go through.", "You can leave through:", "Go through the door", "", "", "", "Go back"])
    FinalPuzzle1.setText(["Opening the laptop you see a sticky note attached to it.  On it is a password", "What do you do?", "Enter the password", "", "", "", "go back"])
    FinalPuzzle1Pass.setText(["You enter in the password.  Once you've done this the laptop shuts down.  You can't turn it back on.", "...", "Okay", "", "", "", ""]) 

    Area11Look.setText(["Looking around the office you find a desk with a laptop on it.", "You find:", "Laptop", "", "", "", "Go back"])
    Area11Leave.setText(["There are three doors.  The one to your left, The one to your right, and the one in front of you.", "You can leave through:", "The left door", "The right door", "The door in front of you", "", "Go back"])
    FinalPuzzle2.setText(["Opening the laptop you see a sticky note attached to it.  On it is a password", "What do you do?", "Enter the password", "", "", "", "go back"])
    FinalPuzzle2Pass.setText(["You enter in the password.  Once you've done this the laptop shuts down.  You can't turn it back on.", "...", "Okay", "", "", "", ""])

    Area12Look.setText(["Looking around the office you find a desk with a laptop on it.", "You find:", "Laptop", "", "", "", "Go back"])
    Area12Leave.setText(["There is only one door you can go through", "You can leave through:", "Go through the door", "", "", "", "Go back"])
    FinalPuzzle3.setText(["Opening the laptop you see a sticky note attached to it.  On it is a password", "What do you do?", "Enter the password", "", "", "", "go back"])
    FinalPuzzle3Pass.setText(["You enter in the password.  Once you've done this the laptop shuts down.  You can't turn it back on.", "...", "Okay", "", "", "", ""])
    
    BadEnd.setText(["Bad ending.", "", "", "", "", "", ""])
    GoodEnd.setText(["Good ending.", "", "", "", "", "", ""])

    #setting all the button commands in all the story areas:
    
    Start.setCommand([["event", StartLook], ["event", StartLeave], [None], [None], [None]])
    Area1.setCommand([["event", Area1Look], ["event", Area1Leave], [None], [None], [None]])
    Area2.setCommand([["event", Area2Look], ["event", Area2Leave], [None], [None], [None]])
    Area3.setCommand([["event", Area3Look], ["event", Area3Leave], [None], [None], [None]])
    Area4.setCommand([["event", Area4Look], ["event", Area4Leave], [None], [None], [None]])
    Area5.setCommand([["event", Area5Look], ["event", Area5Leave], [None], [None], [None]])
    Area6.setCommand([["event", Area6Look], ["event", Area6Leave], [None], [None], [None]])
    Area7.setCommand([["event", Area7Look], ["event", Area7Leave], [None], [None], [None]])
    Area8.setCommand([["event", Area8Look], ["event", Area8Leave], [None], [None], [None]])
    Area9.setCommand([["event", Area9Look], ["event", Area9Leave], [None], [None], [None]])
    Area10.setCommand([["event", Area10Look], ["event", Area10Leave], [None], [None], [None]])
    Area11.setCommand([["event", Area11Look], ["event", Area11Leave], [None], [None], [None]])
    Area12.setCommand([["event", Area12Look], ["event", Area12Leave], [None], [None], [None]])
    Area13.setCommand([["function", Bomb], [None], [None], [None], [None]])

    #setting all the button commands for all the events:

    StartEvent.setCommand([["go", Start], [None], [None], [None], [None]])
    StartLook.setCommand([[None],[None],[None],[None],["return"]])
    StartLeave.setCommand([["go", Area1],["go", Area2],["go", Area3],[None],["return"]])

    Area1Look.setCommand([[None],[None],[None],[None],["return"]])
    Area1Leave.setCommand([["go", Start],["go", Area4],[None],[None],["return"]])

    Area2Look.setCommand([[None],[None],[None],[None],["return"]])
    Area2Leave.setCommand([["go", Start],["go", Area3],["go", Area4],[None],["return"]])

    Area3Look.setCommand([[None],[None],[None],[None],["return"]])
    Area3Leave.setCommand([["go", Start],["go", Area2],[None],[None],["return"]])

    Area4Look.setCommand([[None],[None],[None],[None],["return"]])
    Area4Leave.setCommand([["go", Area5],["go", Area6],[None],[None],["return"]])

    Area5Look.setCommand([["event flag", "ID card", [], IDCardFound, Area5Look],[None],[None],[None],["return"]])
    Area5Leave.setCommand([["go", Area7],[None],[None],[None],["return"]])
    IDCardFound.setCommand([["give flag", Area5, "ID card", True], [None], [None], [None], [None]])
    
    Area6Look.setCommand([["event flag", "Fingerprint", [], GuardFound, Area6Look],[None],[None],[None],["return"]])
    Area6Leave.setCommand([["go", Area8],[None],[None],[None],["return"]])
    GuardFound.setCommand([["event flag", "Fingerprint", [], GuardTaken, GuardFound], [None], [None], [None], ["return"]])
    GuardTaken.setCommand([["give flag", Area6, "Fingerprint", True], [None], [None], [None], [None]])
    
    Area7Look.setCommand([["event flag", "ID card", [True], Puzzle1, Area7Look],[None],[None],[None],["return"]])
    Area7Leave.setCommand([["go", Area5],["event flag", "Card readers", [1, 4, 3, 2], Puzzle1Pass, Puzzle1Fail],[None],[None],["return"]])
    Puzzle1.setCommand([["give flag", Puzzle1, "Card readers", 1], ["give flag", Puzzle1, "Card readers", 2], ["give flag", Puzzle1, "Card readers", 3], ["give flag", Puzzle1, "Card readers", 4], ["return"]])
    Puzzle1Pass.setCommand([["go", Area9], [None], [None], [None], [None]])
    Puzzle1Fail.setCommand([["give flag", Area7, "Card readers", "clear"], [None], [None], [None], [None]])

    Area8Look.setCommand([[None],[None],[None],[None],["return"]])
    Area8Leave.setCommand([["go", Area6],["event flag", "Fingerprint", [True], Puzzle2Pass, Puzzle2Fail],[None],[None],["return"]])
    Puzzle2Pass.setCommand([["go", Area9], [None], [None], [None], [None]])
    Puzzle2Fail.setCommand([["return"], [None], [None], [None], [None]])

    Area9Look.setCommand([[None],[None],[None],[None],["return"]])
    Area9Leave.setCommand([["go", Area11],[None],[None],[None],["return"]])

    Area10Look.setCommand([["event", FinalPuzzle1],[None],[None],[None],["return"]])
    Area10Leave.setCommand([["go", Area11],[None],[None],[None],["return"]])
    FinalPuzzle1.setCommand([["event flag", "Computers", [], FinalPuzzle1Pass, BadEnd],[None],[None],[None],["return"]])
    FinalPuzzle1Pass.setCommand([["give flag", Area10, "Computers", 1], [None], [None], [None], [None]])

    Area11Look.setCommand([["event", FinalPuzzle2],[None],[None],[None],["return"]])
    Area11Leave.setCommand([["go", Area10],["go", Area12],["go", Area13],[None],["return"]])
    FinalPuzzle2.setCommand([["event flag", "Computers", [1], FinalPuzzle2Pass, BadEnd],[None],[None],[None],["return"]])
    FinalPuzzle2Pass.setCommand([["give flag", Area11, "Computers", 2], [None], [None], [None], [None]])

    Area12Look.setCommand([["event", FinalPuzzle3],[None],[None],[None],["return"]])
    Area12Leave.setCommand([["go", Area11],[None],[None],[None],["return"]])
    FinalPuzzle3.setCommand([["event flag", "Computers", [1, 2], FinalPuzzle3Pass, BadEnd],[None],[None],[None],["return"]])
    FinalPuzzle3Pass.setCommand([["give flag", Area10, "Computers", 3], [None], [None], [None], [None]])

    Area13Look.setCommand([[None],[None],[None],[None],["return"]])
    Area13Leave.setCommand([[None],[None],[None],[None],["return"]])



    global currentScreen
    currentScreen = StartEvent

    GameWindow.update()

    window.mainloop()
        

    
    #pass

def Bomb():
    global CurrentTime
    global GameWindow
    global GoodEnd
    global BadEnd
    global flags
    while(True):
        #TimesUp
        CurrentTime = time()
        if(CurrentTime - Start > Stop):
            TimesUp()
        
        #Buttons
        if(GPIO.input(button1) == GPIO.HIGH):
            led2state = (GPIO.HIGH * (led2state == GPIO.LOW)) + (GPIO.LOW * (led2state == GPIO.HIGH))
        elif(GPIO.input(button2) == GPIO.HIGH):
            led1state = (GPIO.HIGH * (led1state == GPIO.LOW)) + (GPIO.LOW * (led1state == GPIO.HIGH))
            led3state = (GPIO.HIGH * (led3state == GPIO.LOW)) + (GPIO.LOW * (led3state == GPIO.HIGH))
        elif(GPIO.input(button3) == GPIO.HIGH):
            led2state = (GPIO.HIGH * (led2state == GPIO.LOW)) + (GPIO.LOW * (led2state == GPIO.HIGH))
            led4state = (GPIO.HIGH * (led4state == GPIO.LOW)) + (GPIO.LOW * (led4state == GPIO.HIGH))
        elif(GPIO.input(button4) == GPIO.HIGH):
            led3state = (GPIO.HIGH * (led3state == GPIO.LOW)) + (GPIO.LOW * (led3state == GPIO.HIGH))

        #LEDs
        GPIO.output(led1, led1state)
        GPIO.output(led2, led2state)
        GPIO.output(led3, led3state)
        GPIO.output(led4, led4state)

        #Disarm
        if(led1state == GPIO.LOW and led2state == GPIO.LOW and led3state == GPIO.LOW and led4state == GPIO.LOW):
            if(flags["Computers"] == [1, 2, 3]):
                currentScreen = GoodEnd
                GameWindow.update()
                break
            else:
                currentScreen = BadEnd
                GameWindow.update()
                break

def TimesUp():
    global currentScreen
    global GameWindow
    global BadEnd
    currentScreen = BadEnd
    GameWindow.update()

#setting up GPIO

#led1 = 
#led2 = 
#led3 = 
#led4 = 
#led1state = GPIO.HIGH
#led2state = GPIO.HIGH
#led3state = GPIO.LOW
#led4state = GPIO.HIGH
#button1 = 
#button2 = 
#button3 = 
#button4 = 

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(led1, GPIO.OUT)
#GPIO.setup(led2, GPIO.OUT)
#GPIO.setup(led3, GPIO.OUT)
#GPIO.setup(led4, GPIO.OUT)
#GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(button4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Main part of the code:

currentScreen = None
flags = {}
Start = time()
Stop = 300
CurrentTime = time()
GameWindow = None
BadEnd = None
GoodEnd = None
Setup()
