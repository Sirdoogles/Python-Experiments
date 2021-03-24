import visa
from tkinter import *
from tkinter import ttk
import time
import Function_Select as fs
rm = visa.ResourceManager()
print(rm.list_resources())


try:
    my_instrument = rm.open_resource('GPIB0::10::INSTR')

    print(my_instrument.query('*IDN?'))
    #my_instrument.write("APPL:SQUARE 1 KHZ, 3.0 VPP, 0 V")

    

except:
    print("Not Connected. Try again")


root = Tk()
root.title("Function Selection")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Select Function Type").grid(column=1, row=1, sticky=(W, E))

selected = IntVar()

ttk.Radiobutton(mainframe, text="Sin", value = 1, variable = selected).grid(column=1, row=2)
ttk.Radiobutton(mainframe, text="Square", value = 2, variable = selected).grid(column=1, row=3)
ttk.Radiobutton(mainframe, text="Ramp", value = 3, variable = selected).grid(column=1, row=4)
ttk.Radiobutton(mainframe, text="Pulse", value = 4, variable = selected).grid(column=1, row=5)
ttk.Radiobutton(mainframe, text="Noise", value = 5, variable = selected).grid(column=1, row=6)

ttk.Button(mainframe, text="Apply Function", command = fs.set(selected)).grid(column=2, row=1)
#ttk.Button(mainframe, text="Function Preset 1", command=fs.func1).grid(column=3, row=3, sticky=W)
#ttk.Button(mainframe, text="Function Preset 2", command=fs.func2).grid(column=4, row=3, sticky=W)

root.mainloop()