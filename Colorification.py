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



def threadButton():
    threading.Thread(target=updateButton).start()


def updateButton():
    global q
    global rMIN
    global rMAX
    global gMIN
    global gMAX
    global bMIN
    global bMAX

    scanpic = pyautogui.screenshot()            #Takes a picture of the screen
    delay = seconds.get()                       #The amount of time delayed
    oldColor = color.get()
    x = pixelX.get()
    y = pixelY.get()
    scanAccuracy = dropped.get()
    myCordinates = (x , y)

    q=1

    if scanAccuracy == "Exact color":
        print ("We're going exact baby")
        while q == 1:
            time.sleep(delay)
            scanpic = pyautogui.screenshot()
            foundColor = scanpic.getpixel((myCordinates))

                # print (str(oldColor))
                
            if (str(foundColor)) == (str(oldColor)):
                print("colors are matching")
                foundStatus.set("A match has been found!")
                print ("Lez goooo")

            if (str(foundColor)) != (str(oldColor)):
                print("colors are not matching")
                foundStatus.set(" ")

    else:
        while q == 1:
            time.sleep(delay)
            scanpic = pyautogui.screenshot()
            foundColor = scanpic.getpixel((myCordinates))
            if (int(rMIN) < (int(foundColor[0])) < int(rMAX)):
                if (int(gMIN) < (int(foundColor[1])) < int(gMAX)):
                    if (int(bMIN) < (int(foundColor[2])) < int(bMAX)):
                        foundStatus.set("A match has been found!")
                    else: 
                        foundStatus.set(" ")
                else: 
                    foundStatus.set(" ") 
            else: 
                foundStatus.set(" ")  

    

    

          
        
def stop():
    global q
    q = 2
    if q == 2:
        print ("We're slowin down bois")
   
    


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

    print (int(colorRGB[0]))
    print (int(colorRGB[1]))
    print (int(colorRGB[2]))

    rMIN = int(colorRGB[0]) - 10
    rMAX = int(colorRGB[0]) + 10

    gMIN = int(colorRGB[1]) - 10
    gMAX = int(colorRGB[1]) + 10

    bMIN = int(colorRGB[2]) - 10
    bMAX = int(colorRGB[2]) + 10

    print (rMIN)
    print (rMAX)
    print (gMIN)
    print (gMAX)
    print (bMIN)
    print (bMAX)


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
root.wm_title('Colorification v1.1')

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
button1 = Button(root, text="Start", command=threadButton)
button3 = Button(root, text="Stop", command=stop)

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

