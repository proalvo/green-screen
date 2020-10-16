# !/bin/python 3
#
# Show green screen with time from timer-for-freestyle-canoe
#
# Designed for Raspberry Pi 3 B with Raspberry Pi OS, interfacing Arduino Uno through USB/Serial connection
#
# Kari Nykänen
# 15.9.2020
#

from serial import *
from tkinter import *

serialPort = "/dev/ttyUSB_GREENSCREEN" # you can use fixed USB port name if you have made symbolic link to USB0/1. 
# serialPort = "/dev/ttyUSB0"  # you may need to change it to USB1 even if you do not change the cable location 
baudRate = 38400 # make sure that Arduino has the same baud rate
ser = Serial(serialPort , baudRate, timeout=0, writeTimeout=0) #ensure non-blocking

# make a TkInter Window

root = Tk()   
root.wm_title("proalvo - Green Screen")  # as the program is running on full screen, the title is shown only if you are switching programs

root.geometry("1920x1080") # screen size, the same as FullHD

root.attributes("-fullscreen", True) # set the screen to fullscreen
root.config(cursor="none") # hide the mouse cursor
root.bind("<Escape>",  quit) # bind "escape" button to "quit" event

timerValueX = 1700 # position of the timer value
timerValueY = 900 # position of the timer value

w = Canvas(root, width=1920, height=1080, highlightthickness=0) # size of FullHD with no border
w.config(background="#009933",borderwidth=0)   # t background color to sgreen
w.pack() # tarvitseeko?

serBuffer = ""  # variable for the string coming from serial interface 

def quit(event):  # if <Escape> is pressed, then quit the program
  import sys; sys.exit()

def readSerial(): # read the serial port and output the value to screen
    while True:
        c = ser.read() # attempt to read a character from Serial
        
        #was anything read?
        if len(c) == 0:
            break

        serialChar = c.decode('utf-8')  # convert incoming byte to string
        # get the buffer from outside of this function
        
        global serBuffer
        #global serialBuffer
        
        # check if character is a delimeter
        if serialChar == '\r':
            c = '' # don't want returns. chuck it
            
        if serialChar == "\n":

            w.dchars("timerValue", 0,2) # delete the old value from te screen
            w.create_text(timerValueX,timerValueY, text=serBuffer, tags="timerValue", fill="white", font=("Arial", 60, "bold")) # write text to screen
            serBuffer = "" # empty the buffer
        else:
            #serBuffer += c # add to the buffer
            serBuffer = serBuffer + serialChar
    
    root.after(10, readSerial) # check serial again soon

# after initializing serial, an arduino may need a bit of time to reset

root.after(100, readSerial) 

root.mainloop()  # main loop to keep window running
