from Tkinter import *
import tkMessageBox
def quitnow():
    if tkMessageBox.askokcancel("Quit", "Are you sure you want to terminate the PyChat server"):
        root.destroy()
root = Tk()
root.title('Chat Server Panel')
Label(text="Basic Commands").grid(row=0, column=0, columnspan=3)
Button( text='Start') .grid(row=1, column=0, padx=5, pady=5)
Button( text='Stop') .grid(row=1, column=1, padx=5, pady=5)
Button( text='Quit', command=quitnow()) .grid(row=1, column=2, padx=5, pady=5)
root.mainloop()
