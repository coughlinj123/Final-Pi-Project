# Names: John Coughlin, Seth Flowers

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

        self.TextDescription = Label(self.master, text = "Location Description.", bg = "grey", width = 24, height = 5)
        self.TextDescription.grid(row=7, column=0, rowspan=5, columnspan=6, sticky=N+S+E+W)

        self.TextChoices = Label(self.master, text = "Choices", bg = "grey", width = 24, height = 1)
        self.TextChoices.grid(row=0, column=7, columnspan=6, sticky=N+S+E+W)

        self.Button = [None, None, None, None, None]
        self.Button[0] = Button(self.master, bg = "grey", text="Button0", command = lambda:self.process(0), width = 24, height = 1)
        self.Button[0].grid(row=3, column=7, columnspan=6, sticky=N+S+E+W)

        self.Button[1] = Button(self.master, bg = "grey", text="Button1", command = lambda:self.process(1), width = 24, height = 1)
        self.Button[1].grid(row=5, column=7, columnspan=6, sticky=N+S+E+W)

        self.Button[2] = Button(self.master, bg = "grey", text="Button2", command = lambda:self.process(2), width = 24, height = 1)
        self.Button[2].grid(row=7, column=7, columnspan=6, sticky=N+S+E+W)

        self.Button[3] = Button(self.master, bg = "grey", text="Button3", command = lambda:self.process(3), width = 24, height = 1)
        self.Button[3].grid(row=9, column=7, columnspan=6, sticky=N+S+E+W)

        self.Button[4] = Button(self.master, bg = "grey", text="Button4", command = lambda:self.process(4), width = 24, height = 1)
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
        global currentArea
        if(self.ButtonCommand[buttonNumber][0] == None):
            pass
        elif(self.ButtonCommand[buttonNumber][0] == "go"):
            currentArea = self.ButtonCommand[buttonNumber][1]
            self.update()

    def update(self):
        self.setDescription(currentArea.DescriptionText)
        self.setChoices(currentArea.ChoicesText)
        self.setButton(0, currentArea.ButtonText[0])
        self.setButton(1, currentArea.ButtonText[1])
        self.setButton(2, currentArea.ButtonText[2])
        self.setButton(3, currentArea.ButtonText[3])
        self.setButton(4, currentArea.ButtonText[4])
        self.setButtonCommand(0, currentArea.ButtonCommand[0])
        self.setButtonCommand(1, currentArea.ButtonCommand[1])
        self.setButtonCommand(2, currentArea.ButtonCommand[2])
        self.setButtonCommand(3, currentArea.ButtonCommand[3])
        self.setButtonCommand(4, currentArea.ButtonCommand[4])
    

class Area:
    #Class variables

    
    def __init__(self):
        #Instance variables
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

    #def addEvent():
        #pass

    #def addArea():
        #pass,

    #def addSideQuest():
        #pass

#class Events:
    #def __init__(self):
        
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
    Area5 = Area()

    #setting the text in all the story areas:

    Start.setText(["Starting area of the Demo", "Starting area choices:", "Go to Area 1", "Go to Area 2", "Do nothing", "Start Event 1", "Start Event 2"])
    Area1.setText(["This is Area 1, in this area you are\nonly able to go back to the Start", "Area 1 choices:", "Go to Starting area.", "", "", "", ""])
    Area2.setText(["This is Area 2, here you are unable \nto go directly back to start.", "Area 2 choices:", "Go to Area 3", "", "", "", ""])
    Area3.setText(["This is Area 3.", "Area 3 choices:", "Go to Starting area", "Go to Area 2", "", "", ""])
    Area5.setText(["This is Area 5. You are unable to do anything here.", "Area 5 choices:", "", "", "", "", ""])

    #setting all the button commands in all the story areas:
    
    Start.setCommand([["go", Area1], ["go", Area2], [None], [None], [None]])
    Area1.setCommand([["go", Start], [None], [None], [None], [None]])
    Area2.setCommand([["go", Area3], [None], [None], [None], [None]])
    Area3.setCommand([["go", Start], ["go", Area2], [None], [None], [None]])
    Area5.setCommand([[None], [None], [None], [None], [None]])

    #Events:
    
    #Main.addEvent()


    #Chase scene:



    #Timed Events:


    #Side Quests:

    #Main.addSideQuest()




    global currentArea
    currentArea = Start

    GameWindow.update()

    window.mainloop()
        

    
    #pass




#Main part of the code:

currentArea = None
Setup()
