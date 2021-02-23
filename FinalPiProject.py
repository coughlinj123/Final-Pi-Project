# Names: John Coughlin, Seth Flowers 1

# Final Pi Project

# Description:


from tkinter import *

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
        if(self.ButtonCommand[buttonNumber][0] == None):
            pass
        elif(self.ButtonCommand[buttonNumber][0] == "go"):
            currentScreen = self.ButtonCommand[buttonNumber][1]
            self.update()
        elif(self.ButtonCommand[buttonNumber][0] == "event"):
            if(str(currentScreen) == "Event"):
                self.ButtonCommand[buttonNumber][1].Area = currentScreen.Area
                currentScreen = self.ButtonCommand[buttonNumber][1]
                self.update()
            else:
                self.ButtonCommand[buttonNumber][1].Area = currentScreen
                currentScreen = self.ButtonCommand[buttonNumber][1]
                self.update()
        elif(self.ButtonCommand[buttonNumber][0] == "give flag"):
            if(str(currentScreen) == "Event"):
                self.ButtonCommand[buttonNumber][1].Area = currentScreen.Area
                currentScreen = self.ButtonCommand[buttonNumber][1]
                flags[self.ButtonCommand[buttonNumber][2]] = True
                self.update()
            else:
                self.ButtonCommand[buttonNumber][1].Area = currentScreen
                currentScreen = self.ButtonCommand[buttonNumber][1]
                flags[self.ButtonCommand[buttonNumber][2]] = True
                self.update()
        elif(self.ButtonCommand[buttonNumber][0] == "event flag"):
            if(flags[self.ButtonCommand[buttonNumber][2]]):
                if(str(currentScreen) == "Event"):
                    self.ButtonCommand[buttonNumber][1].Area = currentScreen.Area
                    currentScreen = self.ButtonCommand[buttonNumber][1]
                    self.update()
                else:
                    self.ButtonCommand[buttonNumber][1].Area = currentScreen
                    currentScreen = self.ButtonCommand[buttonNumber][1]
                    self.update()
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
    Area4.setText(["Area 4 description", "Area 4 choices:", "Look around", "Leave the area", "", "", ""])
    Area5.setText(["Area 5 description", "Area 5 choices:", "Look around", "Leave the area", "", "", ""])
    Area6.setText(["Area 6 description", "Area 6 choices:", "Look around", "Leave the area", "", "", ""])
    Area7.setText(["Area 7 description", "Area 7 choices:", "Look around", "Leave the area", "", "", ""])
    Area8.setText(["Area 8 description", "Area 8 choices:", "Look around", "Leave the area", "", "", ""])
    Area9.setText(["Area 9 description", "Area 9 choices:", "Look around", "Leave the area", "", "", ""])
    Area10.setText(["Area 10 description", "Area 10 choices:", "Look around", "Leave the area", "", "", ""])
    Area11.setText(["Area 11 description", "Area 11 choices:", "Look around", "Leave the area", "", "", ""])
    Area12.setText(["Area 12 description", "Area 12 choices:", "Look around", "Leave the area", "", "", ""])
    Area13.setText(["Area 13 description", "Area 13 choices:", "Look around", "Leave the area", "", "", ""])

    #Creating all flags:

    global flags
    flags["ID Card"] = False
    flags["Fingerprint"] = False

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
    Area6Look = Event()
    Area6Leave = Event()
    Area7Look = Event()
    Area7Leave = Event()
    Area8Look = Event()
    Area8Leave = Event()
    Area9Look = Event()
    Area9Leave = Event()
    Area10Look = Event()
    Area10Leave = Event()
    Area11Look = Event()
    Area11Leave = Event()
    Area12Look = Event()
    Area12Leave = Event()
    Area13Look = Event()
    Area13Leave = Event()

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
    Area4Look.setText(["Looking around Area 4", "You find:", "", "", "", "", "Go back"])
    Area4Leave.setText(["Text description of exits", "You can leave through:", "Area 5", " Area 6", "", "", "Go back"])
    Area5Look.setText(["Looking around Area 5", "You find:", "", "", "", "", "Go back"])
    Area5Leave.setText(["Text description of exits", "You can leave through:", "Area 7", "", "", "", "Go back"])
    Area6Look.setText(["Looking around Area 6", "You find:", "", "", "", "", "Go back"])
    Area6Leave.setText(["Text description of exits", "You can leave through:", "Area 8", "", "", "", "Go back"])
    Area7Look.setText(["Looking around Area 7", "You find:", "", "", "", "", "Go back"])
    Area7Leave.setText(["Text description of exits", "You can leave through:", "Area 5", "Area 9", "", "", "Go back"])
    Area8Look.setText(["Looking around Area 8", "You find:", "", "", "", "", "Go back"])
    Area8Leave.setText(["Text description of exits", "You can leave through:", "Area 6", "Area 9", "", "", "Go back"])
    Area9Look.setText(["Looking around Area 9", "You find:", "", "", "", "", "Go back"])
    Area9Leave.setText(["Text description of exits", "You can leave through:", "Area 11", "", "", "", "Go back"])
    Area10Look.setText(["Looking around Area 10", "You find:", "", "", "", "", "Go back"])
    Area10Leave.setText(["Text description of exits", "You can leave through:", "Area 11", "", "", "", "Go back"])
    Area11Look.setText(["Looking around Area 11", "You find:", "", "", "", "", "Go back"])
    Area11Leave.setText(["Text description of exits", "You can leave through:", "Area 10", "Area 12", "Area 13", "", "Go back"])
    Area12Look.setText(["Looking around Area 12", "You find:", "", "", "", "", "Go back"])
    Area12Leave.setText(["Text description of exits", "You can leave through:", "Area 11", "", "", "", "Go back"])
    Area13Look.setText(["Looking around Area 13", "You find:", "", "", "", "", "Go back"])
    Area13Leave.setText(["Text description of exits", "You can leave through:", "", "", "", "", "Go back"])

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
    Area13.setCommand([["event", Area13Look], ["event", Area13Leave], [None], [None], [None]])

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
    Area5Look.setCommand([[None],[None],[None],[None],["return"]])
    Area5Leave.setCommand([["go", Area7],[None],[None],[None],["return"]])
    Area6Look.setCommand([[None],[None],[None],[None],["return"]])
    Area6Leave.setCommand([["go", Area8],[None],[None],[None],["return"]])
    Area7Look.setCommand([[None],[None],[None],[None],["return"]])
    Area7Leave.setCommand([["go", Area5],["go", Area9],[None],[None],["return"]])
    Area8Look.setCommand([[None],[None],[None],[None],["return"]])
    Area8Leave.setCommand([["go", Area6],["go", Area9],[None],[None],["return"]])
    Area9Look.setCommand([[None],[None],[None],[None],["return"]])
    Area9Leave.setCommand([["go", Area11],[None],[None],[None],["return"]])
    Area10Look.setCommand([[None],[None],[None],[None],["return"]])
    Area10Leave.setCommand([["go", Area11],[None],[None],[None],["return"]])
    Area11Look.setCommand([[None],[None],[None],[None],["return"]])
    Area11Leave.setCommand([["go", Area10],["go", Area12],["go", Area13],[None],["return"]])
    Area12Look.setCommand([[None],[None],[None],[None],["return"]])
    Area12Leave.setCommand([["go", Area11],[None],[None],[None],["return"]])
    Area13Look.setCommand([[None],[None],[None],[None],["return"]])
    Area13Leave.setCommand([[None],[None],[None],[None],["return"]])

    #Chase scene:



    #Timed Events:


    #Side Quests:

    #Main.addSideQuest()




    global currentScreen
    currentScreen = StartEvent

    GameWindow.update()

    window.mainloop()
        

    
    #pass




#Main part of the code:

currentScreen = None
flags = {}
Setup()
