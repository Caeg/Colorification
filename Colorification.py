import pyautogui
import win32api
import time
import threading
from tkinter import *

q = 0


ss = pyautogui.screenshot()
thePosition = pyautogui.position()
color = ss.getpixel(thePosition)



def threadButton():
    threading.Thread(target=updateButton).start()


def updateButton():
    global q
    scanpic = pyautogui.screenshot()            #Takes a picture of the screen
    delay = seconds.get()                       #The amount of time delayed
    oldColor = color.get()
    x = pixelX.get()
    y = pixelY.get()
    myCordinates = (x , y)

    print (q)
    
    q=1
    while q == 1:
        time.sleep(delay)
        scanpic = pyautogui.screenshot()
        foundColor = scanpic.getpixel((myCordinates))
        print (str(foundColor))
        print (str(oldColor))

        if (str(foundColor)) == (str(oldColor)):
            print("colors are matching")
            foundStatus.set("A match has been found!")
            print ("Lez goooo")

        if (str(foundColor)) != (str(oldColor)):
            print("colors are not matching")
            foundStatus.set(" ")
          
        
def stop():
    global q
    q = 2
    if q == 2:
        print ("We're slowin down bois")
   
    


def getPosition():
    ss = pyautogui.screenshot()
    time.sleep(3)
    thePosition = pyautogui.position()
    colorRGB = ss.getpixel(thePosition)
    label_text.set("Color: " + str(colorRGB) + " X: " + str(thePosition[0]) + " Y: " + str(thePosition[1]))

    

root = Tk()
menu = Menu(root)
root.config(menu=menu)
root.wm_title('Colorification v1.0')

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
label4 = Label(root, textvariable=label_text)                                       #label under button
label5 = Label(root, textvariable=foundStatus)

seconds = IntVar()
color = StringVar()
pixelX = IntVar()
pixelY = IntVar()

entry_1 = Entry(root, textvariable = seconds)                                       #entry 1
entry_2 = Entry(root, textvariable = color)                                         #entry 2                                         
entry_3 = Entry(root, textvariable = pixelX)                                        #entry 3
entry_4 = Entry(root, textvariable = pixelY)                                        #entry 4

# threading.Thread(target=updateButton).run()
button1 = Button(root, text="Start", command=threadButton)
button3 = Button(root, text="stop", command=stop)

button2 = Button(root, text="Get mouse position", command=getPosition)

label1.grid(row=0)
label2.grid(row=1)
label3.grid(row=2)
button1.grid(row=4, column=1)
button3.grid(row=5, column=1)
button2.grid(row=4)
label4.grid(row=5)
label5.grid(row=6)



entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=1)
entry_4.grid(row=3, column=1)


print (q)
root.mainloop()

