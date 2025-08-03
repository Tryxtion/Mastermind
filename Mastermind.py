# Mastermind.py


from random import randint
from tkinter import *
from time import sleep
import os
import sys

root = Tk()
root.title("Mastermind")


# Global Variables
global playing
playing = True
btn = []
btnColor = []
InputColors = []


def play_again():
    global gameOver
    root.destroy()
    endWindow.destroy()
    os.system(f'python "{__file__}"')


def leave_game():
    root.destroy()
    endWindow.destroy()


def restart(result):


    global endWindow
    endWindow = Tk()
    endWindow.title("Play Again")
    endWindow.geometry("275x150")
    
    playagain = Label(endWindow, text="YOU " + result + "\nPLAY AGAIN?", bd=15)
    yesBtn = Button(endWindow, width=40, height=2, text="Yes",
                    command=play_again)
    noBtn = Button(endWindow, width=40, height=2, text="No",
                   command=leave_game)
    
    playagain.grid(row=0, column=1)
    yesBtn.grid(row=3, column=1)
    noBtn.grid(row=4, column=1)

    
    endWindow.mainloop()



def buttonpressed(button): # Sets the color
    global color
    # Check if the color of the button is the same as the color
    if btnColor[button] == color:
        btnColor[button] = "#F0F0F0"
        btn[button].configure(bg=btnColor[button]) # configure changes the bg
    else:
        btn[button].configure(bg=color)
        btnColor[button] = color

def CheckRow(Row):
    for i in range (0, len(btn)):
        # Sets any button that state is NORMAL to DISABLED
        if btn[i]['state'] == NORMAL:
            btn[i]['state'] = DISABLED
        # Sets the buttons in the current row's state to NORMAL
        if btn[i].grid_info()['row'] == Row:
            btn[i]['state'] = NORMAL

def CheckIfInCode(colors):

    output = []
    # Clear the 'x'
    for w in range(4):
        if codeColor[w][0]=="x":
            codeColor[w] = codeColor[w][1:len(codeColor[w])]
        
        
    for i in range(4):
        if colors[i]==codeColor[i]:
            output.append("RED")
            codeColor[i] = "x"+codeColor[i]
            colors[i] = "y"+colors[i]
        
    for i in range(4):
        for m in range(4):
            if colors[i] == codeColor[m]:
                output.append("WHITE")
                codeColor[m] = "x"+codeColor[m]
                break
              
    return(output)


def ChangeRow():
    global Row
    InputColors = []
    for i in range(4):
        color = btnColor[4*Row-4 + i]
        if color == "#F0F0F0":
            return
        InputColors.append(color)
    output = CheckIfInCode(InputColors)
    for i in range(4):
        pins[i+(10-Row)*4].configure(bg=output[i] if i < len(output) else "#808080")
    if output == ["RED"]*4:
        ColorCode()
        restart("WIN")
        return
    Row -= 1
    if Row < 1:
        ColorCode()
        restart("LOSE")
        return
    CheckRow(Row)

def NumToColor(num):
    return ["#FF0000", "#0000FF", "#FFFF00", "#00FF00", "#000000", "#FFFFFF"][num]
    
def ColorCode():
    for i in range(4):
        color = codeColor[i]
        if color[0] != '#':
            color = color[1:]
        codebtn[i].configure(bg=color)

# Make the code slot
#==========================================================

codeColor = [] # codeColor is the color of the code
codebtn = []
for i in range(1, 5): # Creates the 4 buttons the secret code is on
    code = Button(root, width=6, height=3, state=DISABLED, bg="#000000")
    codebtn.append(code)
    codebtn[i-1].grid(row=0, column=i, pady=2)
    codeColor.append(NumToColor(randint(0, 5)))


#ColorCode()

# Make 40 buttons
for i in range(40):
    button = Button(root, state=DISABLED, width=6, height=3,
                    command=lambda m=i:buttonpressed(m), bg="#F0F0F0")
    btn.append(button)
    btnColor.append("#F0F0F0")


# Grid the buttons
row = 1
column = 1
for i in range(0, len(btn)):
    btn[i].grid(row=row, column=column, pady=2)
    column = column + 1
    if column == 5:
        column = 1
        row = row + 1


Row = 10 # Set the row to the most bottom row

CheckRow(Row) # Sets the bottom row to the current row

# Create the ENTER button
enter = Button(root, command=ChangeRow, text="ENTER", width=6, height=2,
                        bg="#F0F0F0")
enter.grid(row=9, column=0)




#==============================COLOR=================================
# Define the color functions
color = "#F0F0F0"

def colorRed():
    global color
    color = "#FF0000"

def colorBlue():
    global color
    color = "#0000FF"
            
def colorWhite():
    global color
    color = "#FFFFFF"
            
def colorBlack():
    global color
    color = "#000000"
            
def colorGreen():
    global color
    color = "#00FF00"
            
def colorYellow():
    global color
    color = "#FFFF00"


# Make the color choices
red = Button(root, text="RED", width=6, height=2, bg="#FF0000",
                activebackground="#FF0000", fg="#00FF00",
                activeforeground="#00FF00", command=colorRed)

blue = Button(root, text="BLUE", width=6, height=2, bg="#0000FF",
                activebackground="#0000FF", fg="#FFFF00",
                activeforeground="#FFFF00", command=colorBlue)

white = Button(root, text="WHITE", width=6, height=2, bg="#FFFFFF",
                activebackground="#FFFFFF", fg="#000000",
                activeforeground="#000000", command=colorWhite)

black = Button(root, text="BLACK", width=6, height=2, bg="#000000",
                activebackground="#000000", fg="#FFFFFF",
                activeforeground="#FFFFFF", command=colorBlack)

green = Button(root, text="GREEN", width=6, height=2, bg="#00FF00",
                activebackground="#00FF00", fg="#FF0000",
                activeforeground="#FF0000", command=colorGreen)

yellow = Button(root, text="YELLOW", width=6, height=2, bg="#FFFF00",
                activebackground="#FFFF00", fg="#0000FF",
                activeforeground="#0000FF", command=colorYellow)

# grid the color choices
red.grid(row=11, column=0, padx=2, pady=2)
blue.grid(row=11, column=1, padx=2, pady=2)
white.grid(row=11, column=2, padx=2, pady=2)
black.grid(row=11, column=3, padx=2, pady=2)
green.grid(row=11, column=4, padx=2, pady=2)
yellow.grid(row=11, column=5, padx=2, pady=2)
#============================================================

pins = []
piny = 608
pinx = 285
xchange = 0
ychange = 0


for i in range(0, 10):
    for i in range(0, 4):
        pin = Label(root, bg='#000000', width=1, height=1)
        pins.append(pin)



count=0

for o in range(0, len(pins)):
    pins[o].place(x=pinx+xchange, y=piny+ychange)
    if xchange == 0:
        xchange = 14
    elif xchange == 14:
        xchange = 0
            
    if ychange == 0 and xchange==14:
        ychange = 22
    elif ychange == 22 and xchange==14:
        ychange = 0
        
    count = count+1
    if count==4:
        piny = piny-60
        count = 0




mainloop()





