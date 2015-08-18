#!/usr/bin/python

from Tkinter import *
import csv
import sys

root = Tk()

# If you only want to remove max, min and resize button below line is sufficient  
#root.overrideredirect(True)
# above line will helpful in designing flash screens

# To display the screen in full screen mode
root.attributes("-fullscreen", True) 

#Edit formBg.gif to feature your logo and frame the buttons nicely
#Make sure formBg.gif's dimensions match those of the screen you're showing the form on
photo = PhotoImage(file = './formBg.gif')

BG = Label(image=photo)
BG.image = photo # keep a reference!
BG.place(relx=0.5, rely=0.5, anchor=CENTER)

#Edit these values to tweak label/font colors
labelColor = "#%02x%02x%02x" % (81,16,3) #You'll probably want this color to match the background the label is sitting on
fontColor = "#%02x%02x%02x" % (231,214,189)

#Edit these numbers to tweak positions for entry fields, labels, and the submit button
label1PosX = 940
label1PosY = 30

Entry1PosX = 940
Entry1PosY = 50

label2PosX = 940
label2PosY = 90

Entry2PosX = 940
Entry2PosY = 110

SubmitPosX = 940
SubmitPosY = 150

#Assembling the form

label1 = Label( root, bg=labelColor, fg=fontColor, text="Name")
E1 = Entry(root, bd =1)

label2 = Label( root, bg=labelColor, fg=fontColor, text="Email Address")
E2 = Entry(root, bd =1)
    
def storeData():
   
   if not E1.get():
      E1Clean = 'NULL'
   else:
      for char in E1.get():
         E1Clean = E1.get().translate(None, '!#$%^&*()=?/}]|{[<>,~`"') #If you don't want to remove some of these characters, just delete the ones you want to keep from between the ''
   if not E2.get():
      E2Clean = 'NULL'
   else:
      for char in E2.get():
         E2Clean = E2.get().translate(None, '!#$%^&*()=?/}]|{[<>,~`"') #If you don't want to remove some of these characters, just delete the ones you want to keep from between the ''

   blank = 'NULL'
   data = [blank + "," + E1Clean + "," + E2Clean + "," + blank]
    
   with open('EmailList.csv', 'a') as csvfile:
      spamwriter = csv.writer(csvfile,
                  quotechar='|', quoting=csv.QUOTE_MINIMAL)
      spamwriter.writerow(data)
   #Uncomment these to see a printout of the csv text in the console. In case you need to debug stuff.
   #print E1.get()
   #print E2.get()
   E1.delete(0, END)
   E2.delete(0, END)

submit = Button(root, text ="Submit", command = storeData)

label1.place(x=label1PosX,y=label1PosY)
E1.place(x=Entry1PosX,y=Entry1PosY)
label2.place(x=label2PosX,y=label2PosY)
E2.place(x=Entry2PosX,y=Entry2PosY)
submit.place(x=SubmitPosX,y=SubmitPosY)


root.mainloop()
