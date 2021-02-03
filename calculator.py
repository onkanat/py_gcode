#!/usr/bin/env python
#-*-coding:utf-8-*-



from tkinter import *

class Uygulama(object):
    def __init__(self):
        self.guiPenAr()
        self.gV()

    def gV(self):
        self.depo = ""

    def guiPenAr(self):
        self.ekran = Entry(width=20)
        self.ekran.grid(row=0, column=0, columnspan=3,ipady=4)

        self.liste = [\
                    "9", "8", "7",
                    "6", "5", "4",
                    "3", "2", "1",
                    "0", "+", "-",
                    "/", "*", "=",
                    "C"]

        self.sira = 1
        self.sutun = 0

        for i in self.liste:
            self.komut = lambda x=i: self.hesapla(x)
            Button(text=i,
                   width=5,
                   relief=GROOVE,
                   command=self.komut).grid(row=self.sira,
                                            column=self.sutun)
            self.sutun += 1

            if self.sutun > 2:
                self.sutun = 0
                self.sira += 1

    def hesapla(self, tus):
        self.tus = tus
        if self.tus in "0123456789":
            self.ekran.insert(END,self.tus)
            self.depo = self.depo + self.tus

        if self.tus in "+-/*":
            self.depo = self.depo + self.tus
            self.ekran.delete(0,END)

        if self.tus == "=":
            self.ekran.delete(0,END)
            self.hesap = eval(self.depo,{"__builtins__":None},{})
            self.depo = str(self.hesap)
            self.ekran.insert(END,self.depo)

        if self.tus == "C":
            self.ekran.delete(0,END)
            self.depo = ""

pencere = Tk()
pencere.resizable(width=FALSE,height=FALSE)
uyg = Uygulama()

mainloop()
