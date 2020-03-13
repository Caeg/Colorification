import pyautogui
import win32api
import time
import threading
from tkinter import *

q = 0

rMIN = 0
gMIN = 0
bMIN = 0

rMAX = 0
gMAX = 0
bMAX = 0

ss = pyautogui.screenshot()
thePosition = pyautogui.position()
color = ss.getpixel(thePosition)

def threadStart():
    threading.Thread(target=updateButton).start()

def threadStop():
    threading.Thread(target=stop).start()


def updateButton():
    global q
    global rMIN
    global rMAX
    global gMIN
    global gMAX
    global bMIN
    global bMAX

    scanpic = pyautogui.screenshot()                                #Takes a picture of the screen
    delay = seconds.get()                                           #The amount of time delayed
    oldColor = color.get()                                          #Sets oldcolor to the textbox color
    x = pixelX.get()                                                #Sets x to the textbox x cordinate
    y = pixelY.get()                                                #Sets y to the textbox y cordinate
    scanAccuracy = dropped.get()                                    #Sets the accuracy to what ever is selected in the text box.
    myCordinates = (x , y)                                          #Sets your x y cordinates into one variable 

    q=1                                                             #Value to start the scan

    if scanAccuracy == "Running: Exact color":                               #Loop for Exact color scan             
        while q == 1:       
            time.sleep(delay)                                       #Delay for each scan          
            scanpic = pyautogui.screenshot()                        #Takes picture of screen
            foundColor = scanpic.getpixel((myCordinates))           #Grabs pixel from desired cordinate
                
            if (str(foundColor)) == (str(oldColor)):                #Statement to check if color is found
                foundStatus.set("Running: A match has been found!")          #Notifies user that color is found

            else:                                                   #Else if color is not found
                foundStatus.set("Running: No match found")                                #Removes notification

    else:
        while q == 1:
            time.sleep(delay)
            scanpic = pyautogui.screenshot()
            foundColor = scanpic.getpixel((myCordinates))
            if (int(rMIN) < (int(foundColor[0])) < int(rMAX)):
                if (int(gMIN) < (int(foundColor[1])) < int(gMAX)):
                    if (int(bMIN) < (int(foundColor[2])) < int(bMAX)):
                        foundStatus.set("Running: A match has been found!")
                    else: 
                        foundStatus.set("Running: No match found")
                else: 
                    foundStatus.set("Running: No match found") 
            else: 
                foundStatus.set("Running: No match found")     
        
def stop():
    global q
    delay = seconds.get()
    q = 2
    if q == 2:
        time.sleep(delay + 1)
        foundStatus.set(" ") 
  
   
def getPosition():
    global rMIN
    global rMAX
    global gMIN
    global gMAX
    global bMIN
    global bMAX

    ss = pyautogui.screenshot()
    time.sleep(3)
    thePosition = pyautogui.position()
    colorRGB = ss.getpixel(thePosition)
    label_text.set("Color: " + str(colorRGB) + " X: " + str(thePosition[0]) + " Y: " + str(thePosition[1]))

    rMIN = int(colorRGB[0]) - 15
    rMAX = int(colorRGB[0]) + 15

    gMIN = int(colorRGB[1]) - 15
    gMAX = int(colorRGB[1]) + 15

    bMIN = int(colorRGB[2]) - 15
    bMAX = int(colorRGB[2]) + 15

    if (checked.get() == 1):
        entry_2.delete(0, END)
        entry_2.insert(0, str(colorRGB))
        entry_3.delete(0, END)
        entry_3.insert(0, str(thePosition[0]))
        entry_4.delete(0, END)
        entry_4.insert(0, str(thePosition[1]))

root = Tk()
menu = Menu(root)
root.config(menu=menu)
root.wm_title('Colorification v1.1.1')

btn_text = StringVar()
btn_text.set("Start")

label_text = StringVar()
label_text.set("No current position")
foundStatus = StringVar()
foundStatus.set(" ")

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)

# subMenu.add_command(label="New settings", command=doNothing)
# subMenu.add_command(label="Open settings", command=doNothing)
# subMenu.add_command(label="Save settings", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit)

label1 = Label(root, text="Second delay for each scan:")                            #label row 1
label2 = Label(root, text="What color are you looking to scan? (RGB)")              #label row 2
label3 = Label(root, text="Pixel coordinate you wish to scan:")                     #label row 3
label4 = Label(root, text="Accuracy of color matching:") 
label5 = Label(root, textvariable=label_text)                                       #label under button6
label6 = Label(root, textvariable=foundStatus)
                          
seconds = IntVar()
color = StringVar()
pixelX = IntVar()
pixelY = IntVar()
checked = IntVar()
dropped = StringVar()

entry_1 = Entry(root, textvariable = seconds)                                       #entry 1
entry_2 = Entry(root, textvariable = color)                                         #entry 2                                         
entry_3 = Entry(root, textvariable = pixelX)                                        #entry 3
entry_4 = Entry(root, textvariable = pixelY)                                        #entry 4
dropdown = OptionMenu(root, dropped, "Exact color", "Slight color shift")
dropped.set('Exact color')

entry_2.insert(0, str("(255, 255, 255)"))

# threading.Thread(target=updateButton).run()
button1 = Button(root, text="Start", command=threadStart)
button3 = Button(root, text="Stop", command=threadStop)

button2 = Button(root, text="Get mouse position", command=getPosition)
autoCheck = Checkbutton(root, text="Autofill", onvalue=1, offvalue=0, variable=checked)
checked.set(1)

label1.grid(row=0)                      #"Seconds delayed" text
label2.grid(row=1)                      #"What color" text
label3.grid(row=2)                      #"Pixel coordinate" text
label4.grid(row=4)
button1.grid(row=5, column=1)           # Start button
button3.grid(row=6, column=1)           # Stop button
button2.grid(row=5)                     #"Get Mouse Position" button
autoCheck.grid(row=6)                   # Autofill Check box
label5.grid(row=7)                      #"No current position" text
label6.grid(row=8)                      #"Found" text

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=1)
entry_4.grid(row=3, column=1)
dropdown.grid(row=4, column=1)

root.mainloop()

