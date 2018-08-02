#!/usr/bin/env python2.7
from Tkinter import *

class PianoRoll:

    def __init__(self, master):
        self.master = master
        master.title("Chord Identifer")

        self.label = Label(master, text="Pick 3 notes to create a chord")

        self.piano = Canvas(master,width=300)

        self.cnote = self.piano.create_rectangle(10, 10, 50, 120, fill='#ffffff', activefill='#dc42f4')
        self.dnote = self.piano.create_rectangle(50, 10, 90, 120, fill='#ffffff', activefill='#dc42f4')
        self.enote = self.piano.create_rectangle(90, 10, 130, 120, fill='#ffffff', activefill='#dc42f4')
        self.fnote = self.piano.create_rectangle(130, 10, 170, 120, fill='#ffffff', activefill='#dc42f4')
        self.gnote = self.piano.create_rectangle(170, 10, 210, 120, fill='#ffffff', activefill='#dc42f4')
        self.anote = self.piano.create_rectangle(210, 10, 250, 120, fill='#ffffff', activefill='#dc42f4')
        self.bnote = self.piano.create_rectangle(250, 10, 290, 120, fill='#ffffff', activefill='#dc42f4')
        self.dbnote = self.piano.create_rectangle(40, 10, 60, 70, fill='#000000', activefill='#dc42f4')
        self.ebnote = self.piano.create_rectangle(80, 10, 100, 70, fill='#000000', activefill='#dc42f4')
        self.gbnote = self.piano.create_rectangle(160, 10, 180, 70, fill='#000000', activefill='#dc42f4')
        self.abnote = self.piano.create_rectangle(200, 10, 220, 70, fill='#000000', activefill='#dc42f4')
        self.bbnote = self.piano.create_rectangle(240, 10, 260, 70, fill='#000000', activefill='#dc42f4')

        self.piano.bind('<Button-1>', self.__activate)
        self.piano.bind('<Button-2>', self.__dump)


        # LAYOUT

        self.label.grid(row=0, column=0)
        self.piano.grid(row=1, column=0, padx=20)

    def __activate(self, event):
        event.widget.addtag_closest('active', event.x, event.y)
    

    def __dump(self, event):
        print(self.piano.cnote)


root = Tk()
my_gui = PianoRoll(root)
root.mainloop()
