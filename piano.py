#!/usr/bin/env python2.7
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Setup notes.
        for n in range(0,12):
            getattr(self, 'note_n%s' % n).pressed.connect(lambda v=n: self.input_note(v))

        # Setup operations.
        self.identify_chord.pressed.connect(self.identify)
        self.clear_button.pressed.connect(self.clear)
        self.exit_button.pressed.connect(self.exit)

        self.stack = []
        self.show()

    def display(self):
        self.label_2.setText(''.join(str(e) for e in self.stack))

    def input_note(self, v):
        if(getattr(self,'note_n%s' % v).isChecked()):
            getattr(self, 'note_n%s' % v).setStyleSheet("background-color:#ffffff;")
            getattr(self, 'note_n%s' % v).toggle()
            self.stack.remove(v)
        else:
            getattr(self, 'note_n%s' % v).setStyleSheet("background-color:#ce7fe3;")
            getattr(self, 'note_n%s' % v).toggle()
            self.stack.append(v)

    def identify(self):
        self.notes = [(self.stack[n] - self.stack[0]) for n in range(len(self.stack)-1)]
        self.display()

    def clear(self):
        for n in self.stack:
            getattr(self, 'note_n%s' % n).setStyleSheet("background-color:#ffffff;")
            getattr(self, 'note_n%s' % n).setChecked(False)
        self.stack = []

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Chordy")

    window = MainWindow()
    app.exec_()
