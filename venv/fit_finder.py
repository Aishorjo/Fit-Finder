from tkinter import *

root = Tk()
theLabel = Label(root, text="Welcome to Fit Finder", bg="yellow", fg="black")
theLabel.pack(fill=X)

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="button1", fg="green")
button2 = Button(topFrame, text="button2", fg="blue")
button3 = Button(topFrame, text="button3", fg="orange")
button4 = Button(bottomFrame, text="button4", fg="red")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop()