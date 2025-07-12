from tkinter import * # This is fine for quick scripts, but 'import tkinter as tk' is often preferred

GUI = Tk() # Creates the main window
GUI.title('My accounting app') # Sets the window title
GUI.geometry('500x500') # Sets the window size

L1 = Label(GUI, text='Accounting app') # Creates a label widget
L1.pack() # Places the label in the window using the pack layout manager
L1.configure(font=('Angsana New',20,'bold')) # Sets font properties
L1.configure(fg = 'red') # Sets foreground (text) color
L1.configure(text='Accounting app😎') # Updates the text (this line effectively overwrites the previous 'Accounting app' text)

GUI.mainloop() # Starts the Tkinter event loop - CRUCIAL for the window to appear and stay open